FROM python:3.11
RUN pip install uv
COPY requirements.txt .
RUN uv pip install -r requirements.txt --system