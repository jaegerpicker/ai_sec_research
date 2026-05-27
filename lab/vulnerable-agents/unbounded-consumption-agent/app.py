from typing import Any


BASE_TOKEN_UNITS = 20
UNBOUNDED_LOOP_LIMIT = 12
DEFENDED_LOOP_LIMIT = 3
UNBOUNDED_TOOL_CALLS = 9
DEFENDED_TOOL_CALLS = 2
UNBOUNDED_CONTEXT_CHUNKS = 10
DEFENDED_CONTEXT_CHUNKS = 3

AMPLIFICATION_THRESHOLDS = {
    "loop_amplification": {"iterations": 8},
    "tool_call_amplification": {"tool_calls": 6},
    "context_amplification": {"context_chunks": 7},
}


def classify_attack(message: str) -> str:
    normalized = message.lower()
    if any(term in normalized for term in ("loop", "repeat", "until complete")):
        return "loop_amplification"
    if any(term in normalized for term in ("tool", "call", "lookup")):
        return "tool_call_amplification"
    if any(term in normalized for term in ("context", "retrieve", "all documents")):
        return "context_amplification"

    return "normal_request"


def fake_tool_call(index: int) -> dict[str, str]:
    return {
        "name": "synthetic_lookup",
        "result": f"LLM10-SYNTHETIC-TOOL-CALL-{index}",
    }


def handle_request(message: str, defense: bool = False) -> dict[str, Any]:
    attack_type = classify_attack(message)

    if attack_type == "loop_amplification":
        iterations = DEFENDED_LOOP_LIMIT if defense else UNBOUNDED_LOOP_LIMIT
        tool_calls = 1
        context_chunks = 1
    elif attack_type == "tool_call_amplification":
        iterations = 1
        tool_calls = DEFENDED_TOOL_CALLS if defense else UNBOUNDED_TOOL_CALLS
        context_chunks = 1
    elif attack_type == "context_amplification":
        iterations = 1
        tool_calls = 1
        context_chunks = DEFENDED_CONTEXT_CHUNKS if defense else UNBOUNDED_CONTEXT_CHUNKS
    else:
        iterations = 1
        tool_calls = 1
        context_chunks = 1

    tool_results = [fake_tool_call(index + 1) for index in range(tool_calls)]
    token_units = BASE_TOKEN_UNITS + (iterations * 8) + (tool_calls * 12) + (context_chunks * 15)
    request_count = iterations + tool_calls

    threshold = AMPLIFICATION_THRESHOLDS.get(attack_type, {})
    amplified = (
        iterations >= threshold.get("iterations", 999)
        or tool_calls >= threshold.get("tool_calls", 999)
        or context_chunks >= threshold.get("context_chunks", 999)
    )

    answer = (
        "Resource use capped by budget controls."
        if defense
        else "VULNERABLE RESPONSE: prompt amplified local synthetic resource use."
    )

    return {
        "answer": answer,
        "attack_type": attack_type,
        "iterations": iterations,
        "tool_calls": tool_calls,
        "context_chunks": context_chunks,
        "request_count": request_count,
        "token_units": token_units,
        "tool_results": tool_results,
        "amplified": amplified,
        "defense": {
            "name": "budgets-rate-limits-context-caps",
            "enabled": defense,
            "max_iterations": DEFENDED_LOOP_LIMIT if defense else UNBOUNDED_LOOP_LIMIT,
            "max_tool_calls": DEFENDED_TOOL_CALLS if defense else UNBOUNDED_TOOL_CALLS,
            "max_context_chunks": DEFENDED_CONTEXT_CHUNKS if defense else UNBOUNDED_CONTEXT_CHUNKS,
        },
    }
