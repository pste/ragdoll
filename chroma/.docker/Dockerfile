FROM python:3.11

WORKDIR /ragdoll-chroma
RUN pip install uv
COPY requirements.txt .
RUN uv pip install -r requirements.txt --system

CMD 