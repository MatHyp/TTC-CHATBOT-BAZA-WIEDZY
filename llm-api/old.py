import os
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

APP_API_KEY = os.getenv("APP_PUBLIC_API_KEY")
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
API_KEY_NAME = "X-API-Key"

app = FastAPI(title="Local LLM API Server")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    token=HF_TOKEN,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 512
    temperature: float = 0.7

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == APP_API_KEY:
        return api_key
    raise HTTPException(
        status_code=403, detail="Błąd autoryzacji: Nieprawidłowy klucz publiczny."
    )

@app.post("/v1/generate", dependencies=[Depends(get_api_key)])
async def generate_text(request: ChatRequest):
    try:
        results = pipe(
            request.prompt,
            max_new_tokens=request.max_tokens,
                temperature=request.temperature,
            do_sample=True if request.temperature > 0 else False,
            pad_token_id=tokenizer.eos_token_id
        )
        return {"response": results[0]['generated_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", dependencies=[Depends(get_api_key)])
async def health_check():
    return {"status": "online", "model": MODEL_ID}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.94.207", port=8000)