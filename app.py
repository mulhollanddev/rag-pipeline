import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os

# Ingestão opcional (roda uma vez)
def ingest(pdf_path, persist_directory="./sql_chroma_db"):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = splitter.split_documents(pages)
    st.info(f"Split {len(pages)} pages into {len(chunks)} chunks.")
    embeddings = FastEmbedEmbeddings()
    Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_directory)
    st.success("Ingestão completa!")

# Cria a RAG chain
def rag_chain(persist_directory="./sql_chroma_db"):
    model = ChatOllama(model="llama3:instruct")

    prompt = PromptTemplate.from_template(
        '''
        <s> [Instructions] You are an expert assistant in Wikidata tools. 
        Answer the following question strictly based on the given context, which may contain information about QuickStatements, 
        SPARQL queries, item creation, property formatting, or submission strategies. 
        If the context is insufficient to answer, reply with: "No relevant context available to answer this question." [/Instructions] </s> 

        [Instructions] 
        Question: {input} 
        Context: {context} 
        Answer: 
        [/Instructions]
        '''
    )

    embeddings = FastEmbedEmbeddings()
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5},
    )
    doc_chain = create_stuff_documents_chain(model, prompt)
    chain = create_retrieval_chain(retriever, doc_chain)
    return chain

# Streamlit UI
st.set_page_config(page_title="RAGna: Pergunte sobre Wikidata", page_icon="📚")
st.title("📚 RAGna - Assistente para Wikidata")

# Upload opcional
with st.sidebar:
    st.header("📄 PDF para ingestar")
    uploaded_pdf = st.file_uploader("Envie um PDF para análise", type=["pdf"])
    if uploaded_pdf:
        temp_path = os.path.join("./", uploaded_pdf.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_pdf.read())
        ingest(temp_path)

# Input da pergunta
question = st.text_input("Digite sua pergunta:")

# Processamento
if question:
    chain = rag_chain()
    with st.spinner("Consultando modelo..."):
        response = chain.invoke({"input": question})
        st.markdown("### 🧠 Resposta")
        st.write(response["answer"])

        st.markdown("### 📎 Documentos relevantes")
        for doc in response.get("context", []):
            st.markdown(f"- {doc.metadata.get('source', 'sem origem')} (score: {doc.metadata.get('score', '?')})")
            st.code(doc.page_content[:500] + "...", language="text")
