import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

BASE_DIR = Path(__file__).resolve().parent.parent / "store" / "chroma_db"

chroma_client = chromadb.PersistentClient(
    path= BASE_DIR
)

collection = chroma_client.get_or_create_collection(
    name="book_recommendations"
)

df = pd.read_csv("../Data/processed data/processed_data.csv")

documents = []
metadatas = []
ids = []
for idx, row in df.iterrows():
    content = f"""
    Title: {row['Title']}
    Author: {row['Author']}
    Genre: {row['Genres']}
    Description: {row['Description']}
    """

    documents.append(content)
    metadatas.append({
        "title": row["Title"],
        "author": row["Author"],
        "genre": row["Genres"]
    })
    ids.append(str(idx))

print(f"Total documents to process: {len(documents)}")

print("Generating embeddings...")
embeddings = embedding_model.encode(documents, show_progress_bar=True).tolist()

BATCH_SIZE = 5000
total_batches = (len(documents) + BATCH_SIZE - 1) // BATCH_SIZE

print(f"Adding documents in {total_batches} batches...")
for i in range(0, len(documents), BATCH_SIZE):
    batch_end = min(i + BATCH_SIZE, len(documents))
    batch_num = (i // BATCH_SIZE) + 1
    
    print(f"Processing batch {batch_num}/{total_batches} (documents {i} to {batch_end-1})")
    
    collection.add(
        documents=documents[i:batch_end],
        metadatas=metadatas[i:batch_end],
        ids=ids[i:batch_end],
        embeddings=embeddings[i:batch_end]
    )

print("Vector store built successfully!")
print(f"Total documents added: {len(documents)}")