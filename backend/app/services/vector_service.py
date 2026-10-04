from pathlib import Path
import uuid

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.services.embedding_service import get_embedding_model


CHROMA_PATH = str(
    Path(__file__).resolve().parents[3] / "chroma_db"
)

COLLECTION_NAME = "voicedocs_documents"


def get_vector_store():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embedding_model(),
        persist_directory=CHROMA_PATH
    )


def add_pdf_chunks(filename: str, pages: list):
    """
    Add PDF chunks to ChromaDB.

    Each chunk gets a unique ID so the same PDF
    can be uploaded more than once.
    """

    documents = []
    ids = []

    for page_data in pages:

        page_number = page_data["page"]
        chunks = page_data["chunks"]

        for chunk_index, chunk_text in enumerate(chunks):

            if not chunk_text.strip():
                continue

            document_id = (
                f"{uuid.uuid4()}_"
                f"{filename}_"
                f"page_{page_number}_"
                f"chunk_{chunk_index}"
            )

            document = Document(
                page_content=chunk_text,
                metadata={
                    "filename": filename,
                    "source_type": "pdf",
                    "page": page_number,
                    "chunk_id": document_id
                }
            )

            documents.append(document)
            ids.append(document_id)

    if not documents:
        return 0

    vector_store = get_vector_store()

    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    return len(documents)