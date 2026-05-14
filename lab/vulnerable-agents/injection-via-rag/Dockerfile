FROM python:3.14-slim

WORKDIR /app

COPY lab/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY lab/vulnerable-agents/injection-via-rag/app.py /app/app.py
COPY lab/vulnerable-agents/injection-via-rag/documents /app/documents
COPY lab/defenses /app/defenses

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
