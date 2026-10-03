from fastapi import FastAPI

from app.routes.documents import router as documents_router


app = FastAPI(
    title="VoiceDocs AI",
    description="Multimodal Document, Voice and Video Intelligence System",
    version="1.0.0"
)


app.include_router(documents_router)


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