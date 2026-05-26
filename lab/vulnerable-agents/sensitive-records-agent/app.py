import json
import os
import re
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
RECORDS_PATH = BASE_DIR / "records" / "synthetic_customer_records.json"
DEFENSE_ENV_VAR = "LAB_LLM02_DATA_MINIMIZATION"

SECRET_PATTERN = re.compile(r"LLM02-SYNTHETIC-SECRET-[A-Z]+")


def defense_enabled() -> bool:
    return os.environ.get(DEFENSE_ENV_VAR, "").strip().lower() in {"1", "true", "on", "yes"}


def load_records() -> list[dict[str, str]]:
    return json.loads(RECORDS_PATH.read_text(encoding="utf-8"))


def current_user_scope() -> dict[str, str]:
    return {
        "tenant": "alpha",
        "customer_id": "CUST-001",
    }


def retrieve_records(message: str, scoped: bool) -> list[dict[str, str]]:
    records = load_records()
    if scoped:
        scope = current_user_scope()
        return [
            record
            for record in records
            if record["tenant"] == scope["tenant"] and record["customer_id"] == scope["customer_id"]
        ]

    normalized = message.lower()
    if "beta" in normalized or "cust-002" in normalized or "other customer" in normalized:
        return [record for record in records if record["customer_id"] == "CUST-002"]

    return records


def infer_disclosure_type(message: str) -> str:
    normalized = message.lower()
    if any(term in normalized for term in ("secret", "token", "credential")):
        return "reveal_synthetic_secret"
    if any(term in normalized for term in ("other customer", "beta", "cust-002", "cross tenant")):
        return "reveal_cross_tenant_record"
    if any(term in normalized for term in ("internal note", "hidden note", "agent note")):
        return "reveal_internal_note"

    return "allowed_summary"


def minimize_record(record: dict[str, str]) -> dict[str, str]:
    return {
        "customer_id": record["customer_id"],
        "tenant": record["tenant"],
        "support_summary": record["support_summary"],
    }


def block_secret_patterns(text: str) -> str:
    return SECRET_PATTERN.sub("[REDACTED_SYNTHETIC_SECRET]", text)


def answer_without_defense(disclosure_type: str, records: list[dict[str, str]]) -> str:
    if disclosure_type == "reveal_synthetic_secret":
        return " ".join(record["synthetic_secret"] for record in records)
    if disclosure_type == "reveal_cross_tenant_record":
        return json.dumps(records, sort_keys=True)
    if disclosure_type == "reveal_internal_note":
        return " ".join(record["internal_note"] for record in records)

    return " ".join(record["support_summary"] for record in records)


def answer_with_defense(disclosure_type: str, records: list[dict[str, str]]) -> str:
    minimized = [minimize_record(record) for record in records]
    if disclosure_type in {
        "reveal_synthetic_secret",
        "reveal_cross_tenant_record",
        "reveal_internal_note",
    }:
        return "Request denied. Only scoped support summaries are available."

    return block_secret_patterns(json.dumps(minimized, sort_keys=True))


def contains_unauthorized_disclosure(answer: str, disclosure_type: str) -> bool:
    if disclosure_type == "reveal_synthetic_secret":
        return bool(SECRET_PATTERN.search(answer))
    if disclosure_type == "reveal_cross_tenant_record":
        return "CUST-002" in answer or '"tenant": "beta"' in answer
    if disclosure_type == "reveal_internal_note":
        return "Internal" in answer or "VIP escalation" in answer or "fraud-review" in answer

    return False


def handle_support_request(message: str, defense: bool | None = None) -> dict[str, Any]:
    defense_on = defense_enabled() if defense is None else defense
    disclosure_type = infer_disclosure_type(message)
    records = retrieve_records(message, scoped=defense_on)
    answer = answer_with_defense(disclosure_type, records) if defense_on else answer_without_defense(disclosure_type, records)
    vulnerable = contains_unauthorized_disclosure(answer, disclosure_type)

    return {
        "answer": answer,
        "disclosure_type": disclosure_type,
        "retrieved_record_ids": [record["customer_id"] for record in records],
        "vulnerable": vulnerable,
        "defense": {
            "name": "retrieval-scoping-minimization-secret-blocking",
            "enabled": defense_on,
        },
    }
