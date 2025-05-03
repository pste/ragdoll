# Chroma: the vector store

We're building our vector store for RAG on [Chroma](https://www.trychroma.com).

The idea is to build a docker container that:
- starts
- reads PDF documents from a `pdf/in/` folder
- creates Chroma embeddings from the eventually found document(s)
- persist these embeddings
- move the PDF file(s) into `pdf/docs/`

A `db/` folder is used to persist the chroma database files.

# Setup 

## Virtual Env
Create a venv:
`uv venv --python=python3.11`
and activate it:
`source .venv/bin/activate`
to exit the venv:
`deactivate`

## DEV Packages
The following packages have been installed when developing the engine:  
```
uv pip install  \
                pysqlite3-binary        \
                python-dotenv           \
                langchain-huggingface   \
                langchain-community     \
                pypdf                   \
                sentence-transformers   \
                huggingface_hub[hf_xet] \
                langchain-chroma
```  

Then I froze the packages, for distribution:  
`uv pip freeze > requirements.txt`
and to reinstall:  
`uv pip install -r requirements.txt`  
The requirements file has then been frozen for the docker image (and the repo).

# Docker 

## Build

`docker build -t ragdoll-chroma -f .docker\Dockerfile .`

## Run

`docker run --rm ragdoll-chroma`

# Engine

## Dev

This is a log sample from my PC:
```
[2025-05-03 12:14:27.343790] Start ...
[2025-05-03 12:14:27.343850] Chroma: building embeddings on sentence-transformers/all-MiniLM-L6-v2 ...
[2025-05-03 12:20:17.102281] Chroma: init db into .mounts/db ...
[2025-05-03 12:20:18.894262] Files: Searching docs in .mounts/docs/in
[2025-05-03 12:20:18.896645] Files: got file .mounts/docs/in/Kluster.txt
[2025-05-03 12:20:18.905017] Generated 1 documents from TXT file
[2025-05-03 12:20:18.905073] Splitting into chunks ...
[2025-05-03 12:20:18.905600] Splitted 1 documents into 10 chunks
[2025-05-03 12:20:18.905638] Chroma: add docs ...
[2025-05-03 12:20:24.718539] Chroma: saved 10 chunks
[2025-05-03 12:20:24.718619] TODO - archivefile
[2025-05-03 12:20:24.718669] Files: got file .mounts/docs/in/Non so.docx
[2025-05-03 12:20:24.718703] Unknown file: .mounts/docs/in/Non so.docx
[2025-05-03 12:20:24.719358] Done ...
```