# from openai import OpenAI

# client = OpenAI(
#     base_url="http://localhost:1234/v1",
#     api_key="lm-studio"  # dummy key
# )

# def generate_recommendation(query, documents, metadatas):
#     context = ""
#     for i, (doc, meta) in enumerate(zip(documents, metadatas), start=1):
#         context += f"""
# Book {i}:
# Title: {meta.get('title')}
# Author: {meta.get('author')}
# Genre: {meta.get('genre')}
# Details: {doc}
# """

#     prompt = f"""
# You are a helpful book recommendation assistant.

# User Query:
# "{query}"

# Based on the following books, recommend the most relevant ones.
# Explain WHY each book is a good match.

# Books:
# {context}

# Answer in a friendly, concise, and engaging way.
# """

#     response = client.chat.completions.create(
#         model="qwen3-8b",
#         messages=[
#             {"role": "system", "content": "You are an expert book recommendation system."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=500
#     )

#     return response.choices[0].message.content



















from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_recommendation(query, documents, metadatas):
    context = ""

    for i, (doc, meta) in enumerate(zip(documents, metadatas), start=1):
        context += f"""
Book {i}:
Title: {meta.get('title')}
Author: {meta.get('author')}
Genre: {meta.get('genre')}
Description: {doc}
"""

    prompt = f"""
You are an expert book recommendation assistant.

User Query:
"{query}"

Using the following books, recommend top 5 most relevant ones.
Explain clearly WHY each book matches the user's interest.

Books:
{context}

Answer in a friendly, concise, and helpful tone.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b", 
        messages=[
            {"role": "system", "content": "You are a book recommendation expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content
