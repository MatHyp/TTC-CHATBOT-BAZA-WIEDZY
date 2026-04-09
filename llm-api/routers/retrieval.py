from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.search import retrival_search

router = APIRouter(prefix="/v1", tags=["Retrieval"])


class ChatRequest(BaseModel):
    prompt: str

@router.post("/retrival")
async def search(request: ChatRequest):
    try:
        result = retrival_search(request.prompt)        
        print(result)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))