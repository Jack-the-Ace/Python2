import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

def build_vector_db():
    # 1. Document Loader
    loader = TextLoader("data/construction_law.txt", encoding="utf-8")
    documents = loader.load()

    # 2. Text Splitter (법률 조항 단위를 고려하여 나누기)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n제", "\n\n", "\n", " "]
    )
    docs = text_splitter.split_documents(documents)

    # 3. Embedding 생성 및 Chroma Vector DB 저장
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # db 폴더에 저장
    Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    print("Vector DB 구축 완료!")

if __name__ == "__main__":
    build_vector_db()