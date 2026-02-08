from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path



def retrieve_books(query, k=10):
    BASE_DIR = Path(__file__).resolve().parent.parent / "store" / "chroma_db"

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    
    chroma_client = chromadb.PersistentClient(
        path= BASE_DIR
    
    )
    collection = chroma_client.get_collection(name="book_recommendations")
    
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    return documents, metadatas

