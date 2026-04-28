from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.search import retrival_search
from src.chatbot import Chatboot 
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv # <-- Import this

load_dotenv() # <-- Add this line

chatbot = Chatboot()

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 19
    temperature: float = 0.7

router = APIRouter(prefix="/v1", tags=["Generate"])

    
@router.post("/generate")
async def generate_text(request: ChatRequest):
    try:
        results = retrival_search(request.prompt)
        context = results[1] 

        prompt = f"""Jesteś pomocnym asystentem AI. Twoim zadaniem jest udzielenie precyzyjnej odpowiedzi na pytanie użytkownika.
                Opieraj swoją odpowiedź WYŁĄCZNIE na poniższym kontekście dostarczonym z bazy wiedzy. Jeśli odpowiedź nie znajduje 
                się w kontekście, poinformuj o tym, nie wymyślaj własnych faktów. Odpowiadaj jak najkrocej sie da
                Kontekst:
                {context}
                Pytanie użytkownika:
                {request.prompt}
                Odpowiedź:"""

        ai_response = chatbot(prompt)
        return {"response": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
