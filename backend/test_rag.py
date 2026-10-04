from app.services.rag_service import answer_question


question = "What is the candidate's education?"


result = answer_question(question)


print("=" * 60)
print("RAG ANSWER")
print("=" * 60)

print("\nANSWER:")
print(result["answer"])

print("\nSOURCES:")

for source in result["sources"]:
    print(
        f"- {source['filename']} "
        f"(Page {source['page']})"
    )