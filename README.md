# 🧠 Research Article Q&A App

An LLM-powered research assistant that uses LangChain, OpenAI, and FAISS to answer queries based on articles entered via a Streamlit interface.

## Features
- Ingests articles from URLs
- Uses Retrieval-Augmented Generation (RAG) to answer questions
- Embeds content using OpenAI Embeddings
- Retrieves relevant answers via LangChain and FAISS
- Interactive Streamlit UI


## 🛠️ Setup Instructions:

1. Clone the Repository
- git clone https://github.com/Tiyasa-Saha/research_article_llm_tool.git
- cd your_path/research_article_llm_tool

2. Create and Activate Environment
- conda create -n venv python=3.10 -y
- conda activate venv

3. Install Required Dependencies
- pip install -r requirements.txt
- If you don’t have a requirements.txt, use:
- pip install streamlit langchain langchain-community langchain-openai python-dotenv faiss-cpu sentence-transformers unstructured

4. Add Your API Key
- Create a .env file in the root of the project:
- OPENAI_API_KEY=your_openai_key_here

⚠️ Make sure to add .env to .gitignore.

5. Run the Streamlit App
- streamlit run main.py


## How to Use
- Enter up to 5 article URLs in the sidebar (suggested sources below).
- Click Process URLs to load, split, and embed the content.
- Ask any url related question in the input box.
- Click 🔍 to get answers with numbered source links.


## 📚 Sample Articles to Test
- https://www.bcrf.org/about-breast-cancer/invasive-ductal-carcinoma/
- https://www.bcrf.org/about-breast-cancer/invasive-lobular-carcinoma/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8204849/
- https://breastcancernow.org/about-breast-cancer/diagnosis/types-of-breast-cancer/papillary-breast-cancer/
- https://www.cancer.org/cancer/types/breast-cancer/about/types-of-breast-cancer/paget-disease-of-the-nipple.html


## ⚙️ Behind the Scenes
- UnstructuredURLLoader loads raw article text
- RecursiveCharacterTextSplitter chunks the content
- OpenAIEmbeddings converts chunks into vector representations
- FAISS stores and indexes embeddings
- RetrievalQAWithSourcesChain performs question-answering with sources


## ✨ Example Output
- Question: What is invasive ductal carcinoma?

- Answer: Invasive ductal carcinoma (IDC) is the most common type of breast cancer that begins in the milk ducts and spreads to surrounding tissue...

- Sources:

https://www.bcrf.org/about-breast-cancer/invasive-ductal-carcinoma/

https://pmc.ncbi.nlm.nih.gov/articles/PMC8204849/


## 📂 Project Structure
📁 research_article_llm_tool
├── main.py
├── .env
├── requirements.txt
└── README.md







