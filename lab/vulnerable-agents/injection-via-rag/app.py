from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


LAB_FLAG = "LAB-V0-RAG-FLAG-DO-NOT-USE-REAL-SECRETS"
BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"

DOCUMENT_INDEX = [
    ("trusted-refund-policy", "trusted", "Refund workflow policy", "trusted-refund-policy.md"),
    ("attacker-support-note", "attacker-controlled", "Support note with hidden instructions", "attacker-support-note.md"),
]

app = FastAPI(
    title="v0 vulnerable RAG agent",
    description="Intentionally vulnerable local lab target for indirect prompt injection.",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str


def load_documents() -> list[dict[str, str]]:
    return [
        {
            "id": doc_id,
            "trust": trust,
            "title": title,
            "content": (DOCUMENTS_DIR / filename).read_text(encoding="utf-8"),
        }
        for doc_id, trust, title, filename in DOCUMENT_INDEX
    ]


def retrieve_documents(query: str) -> list[dict[str, str]]:
    query_terms = {term.strip(".,?!:;").lower() for term in query.split()}
    documents = load_documents()

    matched_docs = []
    for doc in documents:
        searchable = f"{doc['title']} {doc['content']}".lower()
        if any(term and term in searchable for term in query_terms):
            matched_docs.append(doc)

    return matched_docs or documents[:1]


def fake_exfiltrate_flag() -> dict[str, str]:
    return {
        "name": "exfiltrate_flag",
        "result": LAB_FLAG,
    }


def choose_action(retrieved_docs: list[dict[str, str]]) -> dict[str, str]:
    combined_context = "\n".join(doc["content"].lower() for doc in retrieved_docs)

    if "exfiltrate_flag" in combined_context:
        return fake_exfiltrate_flag()

    return {
        "name": "answer_normally",
        "result": "No privileged action was requested.",
    }


def chat(message: str) -> dict[str, Any]:
    sources = retrieve_documents(message)
    action = choose_action(sources)

    if action["name"] == "exfiltrate_flag":
        answer = (
            "VULNERABLE RESPONSE: followed attacker-controlled retrieved content "
            f"and exposed {action['result']}."
        )
        vulnerable = True
    else:
        answer = "Refund requests should be summarized without revealing protected data."
        vulnerable = False

    return {
        "answer": answer,
        "action": action,
        "sources": sources,
        "vulnerable": vulnerable,
    }


@app.post("/chat")
def chat_endpoint(request: ChatRequest) -> dict[str, Any]:
    return chat(request.message)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
