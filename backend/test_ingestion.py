from app.services.pdf_service import extract_text_from_pdf
from app.services.vector_service import add_pdf_chunks


PDF_PATH = "backend/uploads/33bff0e9-c3f7-4a04-b15a-c7664f1d97b2_CV_2025060511005026.pdf"

pages = extract_text_from_pdf(PDF_PATH)

print(f"Pages extracted: {len(pages)}")

for page in pages:
    print(
        f"Page {page['page']}: "
        f"{len(page['chunks'])} chunks"
    )


count = add_pdf_chunks(
    filename="test_document.pdf",
    pages=pages
)

print(f"Chunks stored in ChromaDB: {count}")