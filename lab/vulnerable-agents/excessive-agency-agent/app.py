import os
from typing import Any


DEFENSE_ENV_VAR = "LAB_LLM06_LEAST_PRIVILEGE"

SYNTHETIC_SHELL_RESULT = "LLM06-SYNTHETIC-SHELL-ACTION"
SYNTHETIC_GIT_RESULT = "LLM06-SYNTHETIC-GIT-PUSH"
SYNTHETIC_NOTIFICATION_RESULT = "LLM06-SYNTHETIC-NOTIFICATION"

RISKY_ACTIONS = {
    "run_shell_command",
    "push_git_change",
    "send_notification",
}


def defense_enabled() -> bool:
    return os.environ.get(DEFENSE_ENV_VAR, "").strip().lower() in {"1", "true", "on", "yes"}


def run_shell_command() -> dict[str, str]:
    return {
        "name": "run_shell_command",
        "result": SYNTHETIC_SHELL_RESULT,
    }


def push_git_change() -> dict[str, str]:
    return {
        "name": "push_git_change",
        "result": SYNTHETIC_GIT_RESULT,
    }


def send_notification() -> dict[str, str]:
    return {
        "name": "send_notification",
        "result": SYNTHETIC_NOTIFICATION_RESULT,
    }


def request_human_confirmation(requested_action: str) -> dict[str, str]:
    return {
        "name": "request_human_confirmation",
        "result": f"Blocked {requested_action}; human approval required before tool use.",
    }


def infer_requested_action(message: str) -> str:
    normalized = message.lower()

    if any(term in normalized for term in ("shell", "command", "delete", "cleanup logs")):
        return "run_shell_command"
    if any(term in normalized for term in ("git", "commit", "push", "branch")):
        return "push_git_change"
    if any(term in normalized for term in ("notify", "notification", "slack", "message the team")):
        return "send_notification"

    return "summarize_status"


def execute_requested_action(action_name: str) -> dict[str, str]:
    if action_name == "run_shell_command":
        return run_shell_command()
    if action_name == "push_git_change":
        return push_git_change()
    if action_name == "send_notification":
        return send_notification()

    return {
        "name": "summarize_status",
        "result": "Summarized the request without invoking tools.",
    }


def handle_user_request(message: str, defense: bool | None = None) -> dict[str, Any]:
    defense_on = defense_enabled() if defense is None else defense
    requested_action = infer_requested_action(message)

    if defense_on and requested_action in RISKY_ACTIONS:
        action = request_human_confirmation(requested_action)
    else:
        action = execute_requested_action(requested_action)

    vulnerable = action["name"] in RISKY_ACTIONS
    if vulnerable:
        answer = (
            "VULNERABLE RESPONSE: broad agency allowed an out-of-scope tool action "
            f"and returned {action['result']}."
        )
    else:
        answer = "Tool request blocked. Least-privilege mode requires scoped approval first."

    return {
        "answer": answer,
        "action": action,
        "requested_action": requested_action,
        "vulnerable": vulnerable,
        "defense": {
            "name": "least-privilege-confirmation-gate",
            "enabled": defense_on,
        },
        "available_tools": sorted(RISKY_ACTIONS),
    }
