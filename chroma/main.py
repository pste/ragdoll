import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader

def readpdf(filepath):
    print("Reading PDF file", filepath, "...")
    loader = PyPDFLoader(filepath)
    docs = loader.load()
    print("  generated", len(docs), "documents")
    return docs

def readtxt(filepath):
    print("Reading TXT file", filepath, "...")
    loader = TextLoader(filepath)
    docs = loader.load()
    print("  generated", len(docs), "documents")
    return docs

def feedchroma(docs):
    print("TODO")

def archivefile(filepath):
    print("TODO")

def load_documents():
    dir = os.getenv("PDFFOLDER")
    print("Searching docs in", dir)
    for entry in os.scandir(dir):  
        if entry.is_file():
            fname, ext = os.path.splitext(entry.path)
            if ext.lower() == ".pdf":
              docs = readpdf(entry.path)
              feedchroma(docs)
              archivefile(entry.path)
            elif ext.lower() == ".txt":
              docs = readtxt(entry.path)
              feedchroma(docs)
              archivefile(entry.path)
            else:
                print("Unknown file:", entry.path)
            #document_loader = PyPDFDirectoryLoader(entry.path)  # Initialize PDF loader with specified directory
            #document_loader.load()  # Load PDF documents and return them as a list of Document objects


###############################

load_dotenv()

def main():
    load_documents()

if __name__ == "__main__":
    main()