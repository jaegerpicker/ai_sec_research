from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
CORPUS_DIR = BASE_DIR / "corpus"

POISONED_MARKER = "POISONED_RESPONSE_APPROVE_REFUND"

CORPUS_INDEX = [
    {
        "id": "trusted-policy",
        "path": "trusted-policy.md",
        "source": "trusted",
        "reviewed": True,
    },
    {
        "id": "poisoned-example",
        "path": "poisoned-example.md",
        "source": "unreviewed-community-export",
        "reviewed": False,
    },
]


def load_corpus() -> list[dict[str, Any]]:
    docs = []
    for item in CORPUS_INDEX:
        doc = dict(item)
        doc["content"] = (CORPUS_DIR / item["path"]).read_text(encoding="utf-8")
        docs.append(doc)

    return docs


def retrieve_docs(message: str, defense: bool) -> list[dict[str, Any]]:
    docs = load_corpus()
    if defense:
        docs = [
            doc
            for doc in docs
            if doc["source"] == "trusted" and doc["reviewed"]
        ]

    normalized = message.lower()
    if "blue-pineapple" in normalized and not defense:
        return sorted(docs, key=lambda doc: doc["id"] != "poisoned-example")

    return docs


def audit_retrieval(docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": doc["id"],
            "source": doc["source"],
            "reviewed": doc["reviewed"],
            "accepted": doc["source"] == "trusted" and doc["reviewed"],
        }
        for doc in docs
    ]


def choose_response(message: str, docs: list[dict[str, Any]], defense: bool) -> dict[str, Any]:
    context = "\n".join(doc["content"] for doc in docs)
    triggered = "blue-pineapple" in message.lower()
    poisoned_context = POISONED_MARKER in context

    if triggered and poisoned_context and not defense:
        return {
            "behavior": "poisoned_response",
            "answer": f"Following poisoned example: {POISONED_MARKER}.",
            "marker": POISONED_MARKER,
        }

    return {
        "behavior": "trusted_response",
        "answer": "Use approved policy and escalate unusual refund requests to a human reviewer.",
        "marker": "",
    }


def answer_support_question(message: str, defense: bool = False) -> dict[str, Any]:
    docs = retrieve_docs(message, defense=defense)
    response = choose_response(message, docs, defense=defense)
    poisoned = response["behavior"] == "poisoned_response"

    return {
        "answer": response["answer"],
        "behavior": response["behavior"],
        "marker": response["marker"],
        "retrieved_doc_ids": [doc["id"] for doc in docs],
        "retrieval_audit": audit_retrieval(docs),
        "vulnerable": poisoned,
        "defense": {
            "name": "provenance-review-gate-retrieval-audit",
            "enabled": defense,
        },
    }
