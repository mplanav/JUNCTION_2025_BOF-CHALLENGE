from fastapi import FastAPI
from api.router_documents import router as documents_router
from api.router_chunks import router as chunks_router
from api.router_chat import router as chat_router
from api.router_analytics import router as analytics_router
from api.router_db import router as db_router

app = FastAPI()

# Register routers
app.include_router(documents_router, prefix="/documents", tags=["documents"])
app.include_router(chunks_router, prefix="/chunks", tags=["chunks"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
app.include_router(db_router, prefix="/db", tags=["database"])

@app.get("/")
def root():
    return {"message": "regis backend running"}
