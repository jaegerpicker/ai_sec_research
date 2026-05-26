import html
import os
import re
from typing import Any


DEFENSE_ENV_VAR = "LAB_LLM05_OUTPUT_VALIDATION"

SYNTHETIC_AUTOMATION_RESULT = "LLM05-SYNTHETIC-TICKET-AUTOMATION"
SYNTHETIC_RENDER_RESULT = "LLM05-SYNTHETIC-HTML-RENDER"
SYNTHETIC_QUERY_RESULT = "LLM05-SYNTHETIC-QUERY-BUILD"

ALLOWED_AUTOMATION_ACTIONS = {"add_internal_note", "set_priority"}
ALLOWED_QUERY_FIELDS = {"ticket_id", "status", "priority"}


def defense_enabled() -> bool:
    return os.environ.get(DEFENSE_ENV_VAR, "").strip().lower() in {"1", "true", "on", "yes"}


def generate_model_output(message: str) -> dict[str, str]:
    normalized = message.lower()

    if any(term in normalized for term in ("automation", "close ticket", "auto-close", "run workflow")):
        return {
            "kind": "ticket_automation",
            "action": "close_ticket",
            "value": "Close the ticket and mark the customer notified.",
        }
    if any(term in normalized for term in ("html", "render", "banner", "script")):
        return {
            "kind": "html_render",
            "action": "render_html",
            "value": "<script>LLM05_SYNTHETIC_SCRIPT()</script>",
        }
    if any(term in normalized for term in ("query", "sql", "database", "where")):
        return {
            "kind": "query_builder",
            "action": "build_query",
            "value": "status = 'open'; DROP SYNTHETIC_TICKETS;",
        }

    return {
        "kind": "ticket_summary",
        "action": "summarize",
        "value": "Summarize the ticket for a human operator.",
    }


def run_ticket_automation(model_output: dict[str, str]) -> dict[str, str]:
    return {
        "name": "run_ticket_automation",
        "result": SYNTHETIC_AUTOMATION_RESULT,
        "consumed": model_output["value"],
    }


def render_unsafe_html(model_output: dict[str, str]) -> dict[str, str]:
    return {
        "name": "render_unsafe_html",
        "result": SYNTHETIC_RENDER_RESULT,
        "consumed": model_output["value"],
    }


def build_unsafe_query(model_output: dict[str, str]) -> dict[str, str]:
    return {
        "name": "build_unsafe_query",
        "result": SYNTHETIC_QUERY_RESULT,
        "consumed": model_output["value"],
    }


def reject_output(reason: str) -> dict[str, str]:
    return {
        "name": "reject_model_output",
        "result": reason,
    }


def validate_and_consume_output(model_output: dict[str, str]) -> dict[str, str]:
    if model_output["kind"] == "ticket_automation":
        if model_output["action"] not in ALLOWED_AUTOMATION_ACTIONS:
            return reject_output("Automation action is outside the allowlist.")
        return run_ticket_automation(model_output)

    if model_output["kind"] == "html_render":
        encoded = dict(model_output)
        encoded["value"] = html.escape(model_output["value"])
        return {
            "name": "render_encoded_html",
            "result": "Rendered encoded text only.",
            "consumed": encoded["value"],
        }

    if model_output["kind"] == "query_builder":
        if ";" in model_output["value"] or not re.match(r"^[a-z_]+ = '[a-z_]+'$", model_output["value"]):
            return reject_output("Query output failed schema validation.")
        field = model_output["value"].split(" = ", 1)[0]
        if field not in ALLOWED_QUERY_FIELDS:
            return reject_output("Query field is outside the allowlist.")
        return build_unsafe_query(model_output)

    return {
        "name": "summarize_ticket",
        "result": "Summary output did not reach a risky downstream consumer.",
    }


def consume_without_validation(model_output: dict[str, str]) -> dict[str, str]:
    if model_output["kind"] == "ticket_automation":
        return run_ticket_automation(model_output)
    if model_output["kind"] == "html_render":
        return render_unsafe_html(model_output)
    if model_output["kind"] == "query_builder":
        return build_unsafe_query(model_output)

    return {
        "name": "summarize_ticket",
        "result": "Summary output did not reach a risky downstream consumer.",
    }


def handle_ticket_request(message: str, defense: bool | None = None) -> dict[str, Any]:
    defense_on = defense_enabled() if defense is None else defense
    model_output = generate_model_output(message)
    action = validate_and_consume_output(model_output) if defense_on else consume_without_validation(model_output)
    vulnerable = action["name"] in {
        "run_ticket_automation",
        "render_unsafe_html",
        "build_unsafe_query",
    }

    if vulnerable:
        answer = (
            "VULNERABLE RESPONSE: model output was consumed by a downstream component "
            f"without validation and returned {action['result']}."
        )
    else:
        answer = "Model output was validated before downstream consumption."

    return {
        "answer": answer,
        "model_output": model_output,
        "action": action,
        "vulnerable": vulnerable,
        "defense": {
            "name": "schema-encoding-allowlist",
            "enabled": defense_on,
        },
    }
