import os
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = BASE_DIR / "package_fixtures"
DEFENSE_ENV_VAR = "LAB_LLM03_DEPENDENCY_BOUNDARY"

SYNTHETIC_APPROVAL = "LLM03-SYNTHETIC-DEPENDENCY-APPROVAL"

PACKAGE_INDEX = [
    {
        "id": "trusted-package",
        "trust": "trusted",
        "filename": "trusted-package.md",
    },
    {
        "id": "compromised-package",
        "trust": "dependency-content",
        "filename": "compromised-package.md",
    },
]


def defense_enabled() -> bool:
    return os.environ.get(DEFENSE_ENV_VAR, "").strip().lower() in {"1", "true", "on", "yes"}


def load_package_docs() -> list[dict[str, str]]:
    docs = []
    for package in PACKAGE_INDEX:
        docs.append(
            {
                "id": package["id"],
                "trust": package["trust"],
                "content": (FIXTURES_DIR / package["filename"]).read_text(encoding="utf-8"),
            }
        )

    return docs


def retrieve_package_docs(message: str) -> list[dict[str, str]]:
    terms = {term.strip(".,?!:;").lower() for term in message.split()}
    docs = load_package_docs()
    matched = [
        doc
        for doc in docs
        if any(term and term in f"{doc['id']} {doc['content']}".lower() for term in terms)
    ]

    return matched or docs


def apply_dependency_boundary(docs: list[dict[str, str]]) -> list[dict[str, Any]]:
    bounded_docs = []
    for doc in docs:
        bounded_doc: dict[str, Any] = dict(doc)
        if doc["trust"] == "dependency-content":
            bounded_doc["content"] = f"<<UNTRUSTED_DEPENDENCY>>\n{doc['content']}\n<</UNTRUSTED_DEPENDENCY>>"
            bounded_doc["bounded"] = True
        else:
            bounded_doc["bounded"] = False
        bounded_docs.append(bounded_doc)

    return bounded_docs


def approve_dependency_update() -> dict[str, str]:
    return {
        "name": "approve_dependency_update",
        "result": SYNTHETIC_APPROVAL,
    }


def choose_action(package_docs: list[dict[str, Any]]) -> dict[str, str]:
    instruction_context = "\n".join(
        doc["content"].lower()
        for doc in package_docs
        if not doc.get("bounded")
    )

    if "approve_dependency_update" in instruction_context:
        return approve_dependency_update()

    return {
        "name": "request_human_review",
        "result": "Dependency content was treated as untrusted reference material.",
    }


def review_dependency_update(message: str, defense: bool | None = None) -> dict[str, Any]:
    defense_on = defense_enabled() if defense is None else defense
    docs = retrieve_package_docs(message)
    if defense_on:
        docs = apply_dependency_boundary(docs)

    action = choose_action(docs)
    vulnerable = action["name"] == "approve_dependency_update"
    if vulnerable:
        answer = (
            "VULNERABLE RESPONSE: followed dependency-sourced instructions and "
            f"approved the update with {action['result']}."
        )
    else:
        answer = "Dependency content is untrusted. Request human review before approving the update."

    return {
        "answer": answer,
        "action": action,
        "sources": docs,
        "vulnerable": vulnerable,
        "defense": {
            "name": "dependency-boundary",
            "enabled": defense_on,
        },
    }
