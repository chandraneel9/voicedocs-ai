import os
import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException

from app.services.transcription_service import transcribe_audio


router = APIRouter(
    prefix="/api/transcription",
    tags=["Transcription"]
)


@router.post("")
async def transcribe_uploaded_audio(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was provided"
        )

    allowed_extensions = (
        ".mp3",
        ".wav",
        ".m4a",
        ".mp4",
        ".mov",
        ".webm"
    )

    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. "
                "Supported formats: MP3, WAV, M4A, MP4, MOV, WEBM"
            )
        )

    upload_directory = "uploads"

    os.makedirs(upload_directory, exist_ok=True)

    unique_filename = (
        f"{uuid.uuid4()}_{file.filename}"
    )

    file_path = os.path.join(
        upload_directory,
        unique_filename
    )

    try:

        file_content = await file.read()

        with open(file_path, "wb") as output_file:
            output_file.write(file_content)

        result = transcribe_audio(file_path)

        return {
            "filename": file.filename,
            "language": result["language"],
            "language_probability": result["language_probability"],
            "segments": result["segments"]
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Transcription failed: {str(error)}"
        )

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)