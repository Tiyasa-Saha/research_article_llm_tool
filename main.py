import os
import streamlit as st
import pickle
import time
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

st.title("Article Research Tool 📈")
st.sidebar.title("Article URLs")

urls = []
for i in range(5):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# Center-align the "Process URLs" button using columns
col1, col2, col3 = st.sidebar.columns([1, 2, 1])
with col2:
    process_url_clicked = st.button("Process URLs")  # centered in sidebar

file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

# Create two columns: one for input, one for button
col1, col2 = st.columns([5, 1])  # Wider input, narrower button

with col1:
    query = st.text_input("Question:", placeholder="Ask a cancer-related question...", label_visibility="collapsed")

with col2:
    search_clicked = st.button("🔍", help="Search")

if query and search_clicked:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                # Split by comma and remove any extra whitespace
                sources_list = [s.strip() for s in sources.split(',') if s.strip()]

                # Display each source with a number
                for i, source in enumerate(sources_list, start=1):
                    st.markdown(f"{i}. {source}")