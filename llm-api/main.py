from fastapi import FastAPI
from routers.generate import router as generate_router
from routers.retrieval import router as search
app = FastAPI(title="TTC knowledge base")

app.include_router(generate_router)
app.include_router(search)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)