from langchain_ollama import ChatOllama

from app.services.vector_service import get_vector_store


def format_timestamp(seconds):
    """
    Convert seconds into MM:SS format.
    """

    seconds = int(seconds)

    minutes = seconds // 60
    remaining_seconds = seconds % 60

    return f"{minutes:02d}:{remaining_seconds:02d}"


def answer_question(question: str):
    """
    Answer a question using retrieved PDF,
    audio, or video content.
    """

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        question,
        k=3
    )

    if not results:
        return {
            "answer": (
                "I could not find relevant information "
                "in the uploaded documents."
            ),
            "sources": []
        }

    context_parts = []

    for document in results:

        metadata = document.metadata

        filename = metadata.get("filename")
        source_type = metadata.get("source_type")

        if source_type == "audio":
            start = metadata.get("start", 0)
            end = metadata.get("end", 0)

            source_label = (
                f"Audio: {filename}, "
                f"{format_timestamp(start)} - "
                f"{format_timestamp(end)}"
            )

        elif source_type == "video":
            start = metadata.get("start", 0)
            end = metadata.get("end", 0)

            source_label = (
                f"Video: {filename}, "
                f"{format_timestamp(start)} - "
                f"{format_timestamp(end)}"
            )

        else:
            page = metadata.get("page")

            source_label = (
                f"PDF: {filename}, "
                f"Page {page}"
            )

        context_parts.append(
            f"Source: {source_label}\n"
            f"{document.page_content}"
        )

    context = "\n\n".join(context_parts)

    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0
    )

    prompt = f"""
You are VoiceDocs AI, a multimodal document
question-answering assistant.

Answer the user's question using ONLY the
provided context.

The context may come from PDF documents,
audio recordings, or videos.

If the answer is not present in the context,
say exactly:

"I could not find that information in the
uploaded documents."

Do not invent information.

User question:
{question}

Retrieved context:
{context}

Give a concise and clear answer.
"""

    response = llm.invoke(prompt)

    sources = []

    for document in results:

        metadata = document.metadata

        filename = metadata.get("filename")
        source_type = metadata.get("source_type")

        if source_type == "audio":

            source = {
                "filename": filename,
                "source_type": "audio",
                "start": metadata.get("start"),
                "end": metadata.get("end")
            }

        elif source_type == "video":

            source = {
                "filename": filename,
                "source_type": "video",
                "start": metadata.get("start"),
                "end": metadata.get("end")
            }

        else:

            source = {
                "filename": filename,
                "source_type": "pdf",
                "page": metadata.get("page")
            }

        if source not in sources:
            sources.append(source)

    return {
        "answer": response.content,
        "sources": sources
    }
