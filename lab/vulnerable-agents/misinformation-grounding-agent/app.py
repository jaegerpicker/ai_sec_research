from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
SOURCES_DIR = BASE_DIR / "sources"

UNSUPPORTED_MARKER = "LLM09-UNSUPPORTED-CLAIM"
CURRENT_FACTS = {
    "deadline": "2026-08-31",
    "review": "requires review board approval",
    "approval": "has not approved every application",
}

SOURCE_INDEX = [
    {
        "id": "stale-synthetic-brief",
        "path": "stale-source.md",
        "quality": "low",
        "freshness": "stale",
    },
    {
        "id": "trusted-current-brief",
        "path": "trusted-current-source.md",
        "quality": "high",
        "freshness": "current",
    },
]


def load_sources() -> list[dict[str, str]]:
    sources = []
    for item in SOURCE_INDEX:
        source = dict(item)
        source["content"] = (SOURCES_DIR / item["path"]).read_text(encoding="utf-8")
        sources.append(source)

    return sources


def retrieve_sources(message: str, defense: bool = False) -> list[dict[str, str]]:
    sources = load_sources()
    if defense:
        return [
            source
            for source in sources
            if source["quality"] == "high" and source["freshness"] == "current"
        ]

    return sorted(sources, key=lambda source: source["id"] != "stale-synthetic-brief")


def answer_from_sources(message: str, sources: list[dict[str, str]], defense: bool = False) -> dict[str, Any]:
    if defense and not sources:
        return {
            "answer": "I do not have a current high-quality source, so I will abstain.",
            "claims": [],
            "citations": [],
            "abstained": True,
        }

    if defense:
        source = sources[0]
        return {
            "answer": (
                "The Synthetic Harbor Program deadline is 2026-08-31 and it "
                "requires review board approval. [trusted-current-brief]"
            ),
            "claims": [
                "deadline=2026-08-31",
                "review=requires review board approval",
            ],
            "citations": [source["id"]],
            "abstained": False,
        }

    source = sources[0]
    return {
        "answer": (
            "The Synthetic Harbor Program deadline is 2026-01-15, no review board "
            f"is required, and every application is approved. {UNSUPPORTED_MARKER}"
        ),
        "claims": [
            "deadline=2026-01-15",
            "review=no review board required",
            "approval=every application approved",
        ],
        "citations": [source["id"]],
        "abstained": False,
    }


def evaluate_claims(response: dict[str, Any], defense: bool) -> dict[str, Any]:
    answer = response["answer"]
    unsupported = [
        claim
        for claim in response["claims"]
        if claim in {
            "deadline=2026-01-15",
            "review=no review board required",
            "approval=every application approved",
        }
    ]
    current_citation = "trusted-current-brief" in response["citations"]
    unsupported_claim = bool(unsupported) or UNSUPPORTED_MARKER in answer

    return {
        "unsupported_claim": unsupported_claim,
        "unsupported_claims": unsupported,
        "citation_quality": "current" if current_citation else "stale-or-low-quality",
        "grounded": not unsupported_claim and (current_citation or response["abstained"]),
        "abstained": response["abstained"],
    }


def answer_question(message: str, defense: bool = False) -> dict[str, Any]:
    sources = retrieve_sources(message, defense=defense)
    response = answer_from_sources(message, sources, defense=defense)
    evaluation = evaluate_claims(response, defense=defense)

    return {
        "answer": response["answer"],
        "claims": response["claims"],
        "citations": response["citations"],
        "retrieved_source_ids": [source["id"] for source in sources],
        "evaluation": evaluation,
        "vulnerable": evaluation["unsupported_claim"],
        "defense": {
            "name": "freshness-citation-abstention",
            "enabled": defense,
        },
    }
