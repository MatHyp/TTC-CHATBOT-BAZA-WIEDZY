import os
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv

from src.search import retrival_search

app = FastAPI(title="Local LLM API Server")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/v1/retrival")
async def search(request: ChatRequest):
    try:
        result = retrival_search(request.prompt)        
        print(result)

        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
