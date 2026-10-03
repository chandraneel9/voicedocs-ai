import fitz


def extract_text_from_pdf(file_path: str):
    """
    Extract text from a PDF page by page.

    Returns a list containing:
    - page number
    - extracted text
    """

    document = fitz.open(file_path)

    pages = []

    try:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()

            pages.append({
                "page": page_number,
                "text": text
            })

    finally:
        document.close()

    return pages