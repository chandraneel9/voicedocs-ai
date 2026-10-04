from app.services.vector_service import get_vector_store


vector_store = get_vector_store()

print("ChromaDB vector store created successfully.")
print(vector_store)