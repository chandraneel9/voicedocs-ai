import os
import uuid

from app.services.transcription_service import transcribe_audio
from app.services.vector_service import get_vector_store

from langchain_core.documents import Document


def process_audio_file(
    file_path: str,
    filename: str
):
    """
    Transcribe an audio or video file and store
    timestamped transcript segments in ChromaDB.
    """

    transcription = transcribe_audio(file_path)

    segments = transcription["segments"]

    file_extension = os.path.splitext(
        filename
    )[1].lower()

    if file_extension in (
        ".mp4",
        ".mov",
        ".webm"
    ):
        source_type = "video"
    else:
        source_type = "audio"

    documents = []
    ids = []

    for index, segment in enumerate(segments):

        text = segment["text"].strip()

        start = segment["start"]
        end = segment["end"]

        if not text:
            continue

        document_id = (
            f"{uuid.uuid4()}_"
            f"{filename}_"
            f"segment_{index}"
        )

        document = Document(
            page_content=text,
            metadata={
                "filename": filename,
                "source_type": source_type,
                "start": start,
                "end": end,
                "segment_id": document_id
            }
        )

        documents.append(document)
        ids.append(document_id)

    if documents:

        vector_store = get_vector_store()

        vector_store.add_documents(
            documents=documents,
            ids=ids
        )

    return {
        "filename": filename,
        "source_type": source_type,
        "language": transcription["language"],
        "language_probability": transcription[
            "language_probability"
        ],
        "segments": segments,
        "indexed_segments": len(documents)
    }