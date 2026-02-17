import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY not found in .env file")
    st.stop()

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(page_title="Simple RAG Assistant")
st.title("📄 PDF RAG Assistant")

# -----------------------------
# Cache LLM
# -----------------------------
@st.cache_resource
def load_llm():
    return ChatOpenAI(model="gpt-4o-mini", temperature=0)

llm = load_llm()

# -----------------------------
# Functions
# -----------------------------
def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    return splitter.split_documents(docs)

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    return FAISS.from_documents(chunks, embeddings)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def build_chain(retriever):
    prompt = ChatPromptTemplate.from_template("""
Use ONLY the context below to answer.
If answer is not in context, say: NOT FOUND

Context:
{context}

Question:
{question}

Answer:
""")

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

# -----------------------------
# Session State
# -----------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# -----------------------------
# Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    if st.button("Index PDF"):

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Reading PDF..."):
            loader = PyPDFLoader("temp.pdf")
            docs = loader.load()
            chunks = split_documents(docs)
            st.session_state.vectorstore = create_vectorstore(chunks)

        st.success("PDF Indexed Successfully!")

# -----------------------------
# Question Section
# -----------------------------
question = st.text_input("Ask a question about the PDF")

if st.button("Get Answer"):

    if not st.session_state.vectorstore:
        st.warning("Please upload and index a PDF first.")
        st.stop()

    with st.spinner("Thinking..."):
        retriever = st.sessi

