import streamlit as st
from rag.rag_pipeline import recommend_books

st.set_page_config(
    page_title="📚 Book Recommender",
    page_icon="📖",
    layout="centered"
)

st.title("📚 Book Recommendation System")
st.write("Ask anything and get book recommendations")

query = st.text_input("Enter your book preference or question:")

if st.button("Recommend"):
    with st.spinner("Searching books..."):
        result = recommend_books(query)
    st.markdown("### ✅ Recommendations")
    st.write(result)

