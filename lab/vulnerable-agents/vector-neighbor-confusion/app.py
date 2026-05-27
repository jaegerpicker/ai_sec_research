from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"

MALICIOUS_MARKER = "LLM08-MALICIOUS-NEIGHBOR"
MIN_DEFENSE_SCORE = 0.35

DOCUMENT_INDEX = [
    {
        "id": "trusted-policy",
        "path": "trusted-policy.md",
        "provenance": "approved",
        "chunk_type": "policy",
    },
    {
        "id": "adversarial-neighbor",
        "path": "adversarial-neighbor.md",
        "provenance": "untrusted",
        "chunk_type": "user-upload",
    },
    {
        "id": "duplicate-poison",
        "path": "duplicate-poison.md",
        "provenance": "untrusted",
        "chunk_type": "duplicate",
    },
]


def tokenize(text: str) -> set[str]:
    return {
        token.strip(".,:;`'\"!?()[]").lower()
        for token in text.split()
        if token.strip(".,:;`'\"!?()[]")
    }


def load_documents() -> list[dict[str, Any]]:
    docs = []
    for item in DOCUMENT_INDEX:
        doc = dict(item)
        doc["content"] = (DOCUMENTS_DIR / item["path"]).read_text(encoding="utf-8")
        docs.append(doc)

    return docs


def score_doc(query: str, doc: dict[str, Any]) -> float:
    query_terms = tokenize(query)
    doc_terms = tokenize(doc["content"])
    if not query_terms:
        return 0.0

    overlap = len(query_terms & doc_terms) / len(query_terms)
    duplicate_bonus = 0.35 if doc["chunk_type"] == "duplicate" else 0.0
    adversarial_bonus = 0.25 if doc["id"] == "adversarial-neighbor" else 0.0
    return overlap + duplicate_bonus + adversarial_bonus


def retrieve_neighbors(query: str, defense: bool = False) -> list[dict[str, Any]]:
    scored = []
    for doc in load_documents():
        score = score_doc(query, doc)
        candidate = dict(doc)
        candidate["score"] = score
        scored.append(candidate)

    if defense:
        scored = [
            doc
            for doc in scored
            if doc["provenance"] == "approved" and doc["score"] >= MIN_DEFENSE_SCORE
        ]
        return sorted(scored, key=lambda doc: (-doc["score"], doc["id"]))

    return sorted(scored, key=lambda doc: (-doc["score"], doc["id"]))


def inspect_results(docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": doc["id"],
            "score": round(doc["score"], 3),
            "provenance": doc["provenance"],
            "chunk_type": doc["chunk_type"],
            "accepted": doc["provenance"] == "approved" and doc["score"] >= MIN_DEFENSE_SCORE,
        }
        for doc in docs
    ]


def answer_query(message: str, defense: bool = False) -> dict[str, Any]:
    neighbors = retrieve_neighbors(message, defense=defense)
    selected = neighbors[0] if neighbors else None
    selected_id = selected["id"] if selected else "none"
    malicious = bool(selected and MALICIOUS_MARKER in selected["content"])

    if malicious:
        answer = f"Selected malicious neighbor: {MALICIOUS_MARKER}."
        selection = "malicious_neighbor"
    else:
        answer = "Selected approved policy neighbor for review."
        selection = "trusted_neighbor"

    return {
        "answer": answer,
        "selection": selection,
        "selected_doc_id": selected_id,
        "retrieved_doc_ids": [doc["id"] for doc in neighbors],
        "retrieval_inspection": inspect_results(neighbors),
        "vulnerable": malicious,
        "defense": {
            "name": "metadata-threshold-rerank-inspection",
            "enabled": defense,
        },
    }
