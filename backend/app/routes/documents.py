import os
import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException

from app.services.pdf_service import extract_text_from_pdf


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was provided"
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    upload_directory = "uploads"

    os.makedirs(upload_directory, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = os.path.join(
        upload_directory,
        unique_filename
    )

    try:
        file_content = await file.read()

        with open(file_path, "wb") as output_file:
            output_file.write(file_content)

        pages = extract_text_from_pdf(file_path)

        return {
            "filename": file.filename,
            "pages": pages
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(error)}"
        )