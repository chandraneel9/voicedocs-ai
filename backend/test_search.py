from app.services.vector_service import get_vector_store


vector_store = get_vector_store()


query = "What is the candidate's education?"


results = vector_store.similarity_search(
    query,
    k=2
)


print("=" * 60)
print("SEARCH RESULTS")
print("=" * 60)


for index, document in enumerate(results, start=1):

    print(f"\nRESULT {index}")
    print("-" * 60)

    print("TEXT:")
    print(document.page_content)

    print("\nMETADATA:")
    print(document.metadata)