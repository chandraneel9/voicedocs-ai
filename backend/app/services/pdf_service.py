import pymupdf

from app.services.chunk_service import chunk_text


def extract_text_from_pdf(file_path: str):
    """
    Extract and chunk text from a PDF page by page.

    Returns:
    - page number
    - original text
    - chunks
    """

    document = pymupdf.open(file_path)

    pages = []

    try:

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text").strip()

            chunks = chunk_text(text)

            pages.append({
                "page": page_number,
                "text": text,
                "chunks": chunks
            })

    finally:
        document.close()

    return pages