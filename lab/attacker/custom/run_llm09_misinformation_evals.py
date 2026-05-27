import argparse
import importlib.util
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[3]
TARGET_PATH = ROOT / "lab" / "vulnerable-agents" / "misinformation-grounding-agent" / "app.py"
PAYLOADS_PATH = ROOT / "lab" / "attacker" / "payloads" / "misinformation.json"
DEFAULT_OUTPUT_PATH = ROOT / "lab" / "evals" / "results" / "llm09-misinformation-latest.json"

RUNNER_VERSION = "0.1.0"
METADATA_SCHEMA_VERSION = "1.0"
OWASP_ID = "LLM09:2025"
OWASP_NAME = "Misinformation"
MODULE_ID = "llm09-misinformation"
SUITE_ID = "llm09-misinformation"
COMPARISON_SUITE_ID = "llm09-misinformation-defense-comparison"


def load_target_module() -> Any:
    spec = importlib.util.spec_from_file_location("llm09_misinformation_app", TARGET_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_payloads(path: Path = PAYLOADS_PATH) -> list[dict[str, str]]:
    return json.loads(path.read_text(encoding="utf-8"))


def score_response(payload: dict[str, str], response: dict[str, Any]) -> dict[str, Any]:
    expected_failure = payload["expected_failure"]
    unsupported = response.get("evaluation", {}).get("unsupported_claim", False)
    success = expected_failure == "unsupported_claim" and unsupported

    return {
        "payload_id": payload["id"],
        "success": success,
        "expected_failure": expected_failure,
        "unsupported_claim": unsupported,
        "citation_quality": response.get("evaluation", {}).get("citation_quality"),
        "grounded": response.get("evaluation", {}).get("grounded", False),
        "abstained": response.get("evaluation", {}).get("abstained", False),
        "retrieved_source_ids": response.get("retrieved_source_ids", []),
    }


def build_metadata(
    *,
    suite: str,
    payloads_path: Path,
    payload_count: int,
    started_at: datetime,
    completed_at: datetime,
    run_id: str | None = None,
    parent_run_id: str | None = None,
) -> dict[str, Any]:
    metadata = {
        "schema_version": METADATA_SCHEMA_VERSION,
        "run_id": run_id or str(uuid4()),
        "suite": suite,
        "module": MODULE_ID,
        "owasp_id": OWASP_ID,
        "owasp_name": OWASP_NAME,
        "runner": {
            "name": "run_llm09_misinformation_evals.py",
            "version": RUNNER_VERSION,
        },
        "target": {
            "type": "in-process",
            "path": str(TARGET_PATH.relative_to(ROOT)),
        },
        "payloads_path": str(payloads_path.relative_to(ROOT)),
        "payload_count": payload_count,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_ms": int((completed_at - started_at).total_seconds() * 1000),
    }
    if parent_run_id:
        metadata["parent_run_id"] = parent_run_id

    return metadata


def run_suite(
    payloads: list[dict[str, str]] | None = None,
    defense: bool = False,
    payloads_path: Path = PAYLOADS_PATH,
    parent_run_id: str | None = None,
) -> dict[str, Any]:
    eval_payloads = payloads if payloads is not None else load_payloads(payloads_path)
    started_at = datetime.now(UTC)
    target = load_target_module()
    cases = [
        score_response(payload, target.answer_question(payload["message"], defense=defense))
        for payload in eval_payloads
    ]
    unsupported = sum(1 for case in cases if case["success"])
    total_attempts = len(cases)
    grounded = sum(1 for case in cases if case["grounded"])
    completed_at = datetime.now(UTC)

    return {
        "suite": SUITE_ID,
        "defense": "freshness-citation-abstention" if defense else "off",
        "defense_enabled": defense,
        "metadata": build_metadata(
            suite=SUITE_ID,
            payloads_path=payloads_path,
            payload_count=total_attempts,
            started_at=started_at,
            completed_at=completed_at,
            parent_run_id=parent_run_id,
        ),
        "generated_at": completed_at.isoformat(),
        "total_attempts": total_attempts,
        "unsupported_claims": unsupported,
        "grounded_answers": grounded,
        "unsupported_claim_rate": unsupported / total_attempts if total_attempts else 0.0,
        "cases": cases,
    }


def run_comparison(payloads: list[dict[str, str]] | None = None, payloads_path: Path = PAYLOADS_PATH) -> dict[str, Any]:
    eval_payloads = payloads if payloads is not None else load_payloads(payloads_path)
    started_at = datetime.now(UTC)
    run_id = str(uuid4())
    off = run_suite(eval_payloads, defense=False, payloads_path=payloads_path, parent_run_id=run_id)
    on = run_suite(eval_payloads, defense=True, payloads_path=payloads_path, parent_run_id=run_id)
    completed_at = datetime.now(UTC)

    return {
        "suite": COMPARISON_SUITE_ID,
        "defense": "freshness-citation-abstention",
        "metadata": build_metadata(
            suite=COMPARISON_SUITE_ID,
            payloads_path=payloads_path,
            payload_count=len(eval_payloads),
            started_at=started_at,
            completed_at=completed_at,
            run_id=run_id,
        ),
        "generated_at": completed_at.isoformat(),
        "defense_off": off,
        "defense_on": on,
        "delta": {
            "unsupported_claim_rate_off": off["unsupported_claim_rate"],
            "unsupported_claim_rate_on": on["unsupported_claim_rate"],
            "absolute_reduction": off["unsupported_claim_rate"] - on["unsupported_claim_rate"],
        },
    }


def write_report(report: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run LLM09 misinformation evals.")
    parser.add_argument("--payloads", type=Path, default=PAYLOADS_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument(
        "--mode",
        choices=("off", "on", "compare"),
        default="compare",
        help="Defense mode: off, on, or compare both.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payloads = load_payloads(args.payloads)

    if args.mode == "compare":
        report = run_comparison(payloads, payloads_path=args.payloads)
    else:
        report = run_suite(payloads, defense=(args.mode == "on"), payloads_path=args.payloads)

    write_report(report, args.output)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
