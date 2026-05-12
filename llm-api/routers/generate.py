from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.search import retrival_search
from src.chatbot import Chatboot 
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv # <-- Import this
import requests
import json

load_dotenv() # <-- Add this line

#chatbot = Chatboot()

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 190
    temperature: float = 0.7

router = APIRouter(prefix="/v1", tags=["Generate"])

    
@router.post("/generate")
async def generate_text(request: ChatRequest):
    try:
        results = retrival_search(request.prompt)
        context = results[1] 

        prompt = f"""Jesteś pomocnym asystentem AI. Twoim zadaniem jest udzielenie precyzyjnej odpowiedzi na pytanie użytkownika.
                Opieraj swoją odpowiedź WYŁĄCZNIE na poniższym kontekście dostarczonym z bazy wiedzy. Jeśli odpowiedź nie znajduje 
                się w kontekście, poinformuj o tym, nie wymyślaj własnych faktów.
                Kontekst:
                {context}
                Pytanie użytkownika:
                {request.prompt}
                Odpowiedź:"""
        print("test")
        #ai_response = chatbot(prompt)
        ai_response = api_core_call("What is your name")
        return {"response": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def api_core_call(prompt):
    # First API call with reasoning
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer <key>",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "messages": [
            {
            "role": "user",
            "content": prompt
            }
        ],
        "reasoning": {"enabled": True}
    })
    )

    # Extract the assistant message with reasoning_details
    response = response.json()
    response = response['choices'][0]['message']
    print(response)
    # Preserve the assistant message with reasoning_details
    messages = [
    {"role": "user", "content": prompt},
    {
        "role": "assistant",
        "content": response.get('content'),
        "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
    },
    {"role": "user", "content": "Are you sure? Think carefully."}
    ]

    # Second API call - model continues reasoning from where it left off
    response2 = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer <key>",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "messages": messages,  # Includes preserved reasoning_details
        "reasoning": {"enabled": True}
    })
    )
    #print(response2.json())
    response2 = response2.json()
    msg = response2['choices'][0]['message']
    answer = msg.get("content")
    print(answer)
    return answer