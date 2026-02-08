from rag.retriver import retrieve_books
from rag.generator import generate_recommendation

def recommend_books(query):
    documents, metadatas = retrieve_books(query)

    if not documents:
        return "Sorry, I couldn't find relevant books."

    response = generate_recommendation(query, documents, metadatas)
    return response


if __name__ == "__main__":
    while True:
        user_query = input("\n📚 Ask for book recommendations (or type 'exit'): ")

        if user_query.lower() == "exit":
            break

        answer = recommend_books(user_query)
        print("\n✨ Recommendations:\n")
        print(answer)
