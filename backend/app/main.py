from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.documents import router as documents_router
from app.routes.chat import router as chat_router
from app.routes.transcription import router as transcription_router
from app.routes.audio import router as audio_router


app = FastAPI(
    title="VoiceDocs AI",
    description="Multimodal Document, Voice and Video Intelligence System",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(documents_router)
app.include_router(chat_router)
app.include_router(transcription_router)
app.include_router(audio_router)


@app.get("/")
def root():
    return {
        "message": "VoiceDocs AI Backend is running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "VoiceDocs AI Backend"
    }