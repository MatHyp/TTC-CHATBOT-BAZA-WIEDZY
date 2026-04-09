from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.search import retrival_search
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv # <-- Import this

# Load environment variables from your .env file
load_dotenv() # <-- Add this line

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 19
    temperature: float = 0.7

router = APIRouter(prefix="/v1", tags=["Generate"])

# Now these will properly grab the values from your .env file
APP_API_KEY = os.getenv("APP_PUBLIC_API_KEY")
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN") 
API_KEY_NAME = "X-API-Key"
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    token=HF_TOKEN,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    
@router.post("/generate")
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
