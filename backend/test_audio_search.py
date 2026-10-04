from app.services.vector_service import get_vector_store


vector_store = get_vector_store()


query = "What is supervised learning?"


results = vector_store.similarity_search(
    query,
    k=3
)


print("=" * 60)
print("AUDIO SEARCH RESULTS")
print("=" * 60)


for index, document in enumerate(
    results,
    start=1
):

    print()
    print(f"RESULT {index}")
    print("-" * 60)

    print("TEXT:")
    print(document.page_content)

    print()
    print("METADATA:")

    print(
        f"Filename: "
        f"{document.metadata.get('filename')}"
    )

    print(
        f"Source Type: "
        f"{document.metadata.get('source_type')}"
    )

    print(
        f"Start: "
        f"{document.metadata.get('start')} seconds"
    )

    print(
        f"End: "
        f"{document.metadata.get('end')} seconds"
    )
