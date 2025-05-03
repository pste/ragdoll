# sqlite3 fix for chroma (RuntimeError: Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0)
import pysqlite3
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

# imports
import os
import datetime
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

## UTILS ###############################

def log(s: str):
    print(f'[{datetime.datetime.now()}] {s}')

def readpdf(filepath: str):
    loader = PyPDFLoader(filepath)
    docs = loader.load()
    log(f"Generated {len(docs)} documents from PDF file")
    return docs

def readtxt(filepath: str):
    loader = TextLoader(filepath)
    docs = loader.load()
    log(f"Generated {len(docs)} documents from TXT file")
    return docs


def splitdocs(documents: list[Document]):
    log(f"Splitting into chunks ...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )

    # 
    chunks = text_splitter.split_documents(documents)
    log(f"Splitted {len(documents)} documents into {len(chunks)} chunks")

    return chunks

def save2chroma(vector_store: Chroma, key: str, chunks: list[Document]):
    log(f"Chroma: add docs ...")
    #db = Chroma.from_documents(
    #    documents=chunks,
    #    embedding_function=sentence_transformer_ef,
    #    persist_directory=dbpath,
    #    ids=[key]
    #)

    #chroma_vector_store.add_documents(documents=chunks)

    _ = vector_store.add_documents(documents=chunks)

    #log("Chroma: persist ...")
    #db.persist()
    log(f"Chroma: saved {len(chunks)} chunks")

## DB ##################################

def initDB():
    # embeddings
    # best quality:
    # model = "sentence-transformers/all-mpnet-base-v2")
    # faster, good quality:
    model = "sentence-transformers/all-MiniLM-L6-v2"
    log(f"Chroma: building embeddings on {model} ...")
    embeddings = HuggingFaceEmbeddings(model_name=model)

    # chroma
    chromadir = os.getenv("FOLDERCHROMA", "./chroma_langchain_db")
    log(f"Chroma: init db into {chromadir} ...")
    vector_store = Chroma(
        collection_name="games_collection",
        embedding_function=embeddings,
        persist_directory=chromadir,
    )
    return vector_store

## ENGINE ################################## 

def feedchroma(db: Chroma, key: str, docs: list[Document]):
    chunks = splitdocs(docs)
    save2chroma(db, key, chunks)

def archivefile(filepath):
    log(f"TODO - archivefile")

def load_documents(db: Chroma):
    dir = os.getenv("FOLDERDOCS")
    log(f"Files: Searching docs in {dir}")
    for entry in os.scandir(dir):  
        if entry.is_file():
            fname, ext = os.path.splitext(entry.path)
            log(f"Files: got file {entry.path}")
            if ext.lower() == ".pdfOFF":
              docs = readpdf(entry.path)
              feedchroma(db, entry.path, docs)
              archivefile(entry.path)
            elif ext.lower() == ".txt":
              docs = readtxt(entry.path)
              feedchroma(db, entry.path, docs)
              archivefile(entry.path)
            else:
                log(f"Unknown file: {entry.path}")

## MAIN #############################

load_dotenv()

def main():
    log(f"Start ...")
    db = initDB()
    load_documents(db)
    log(f"Done ...")

if __name__ == "__main__":
    main()