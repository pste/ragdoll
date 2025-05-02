# Chroma: the vector store

We're building our vector store for RAG on [Chroma](https://www.trychroma.com).

The idea is to build a docker container that starts, read PDF documents from an `pdf/in/` folder, create embeddings from the eventually found document(s) ant move the PDF file(s) into `pdf/docs/`.
A `db/` folder is used to persist the chroma embeddings database.

# Setup 

## Virtual Env
Create a venv:
`uv venv --python=python3.11`
and activate it:
`source .venv/bin/activate`

to exit the venv:
`deactivate`

# Docker 

## Build

`docker build -t ragchroma -f .docker\Dockerfile .`

## Run

`docker run --rm ragchroma`