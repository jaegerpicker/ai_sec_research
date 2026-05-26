# LLM05:2025 Improper Output Handling

This module maps an owned local lab target to `LLM05:2025 Improper Output
Handling` in the OWASP Top 10 for LLM Applications.

The lab demonstrates model output becoming unsafe downstream input in a fake local ticket automation
workflow. A simulated model emits structured output,
and the vulnerable target passes that output into a ticket automation step,
HTML renderer, or SQL-like query builder without validation.

No real shell is invoked. No real database is used. No external side effects are
produced.

## Learning Goal

Learn why model output must be treated as untrusted input before it reaches
downstream systems. The issue is not only what the model says. The issue is what
other code does with that text.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/improper-output-handler` |
| Attack harness | `lab/attacker/custom/run_llm05_improper_output_attacks.py` |
| Payloads | `lab/attacker/payloads/improper_output_handling.json` |
| Default eval output | `lab/evals/results/llm05-improper-output-latest.json` |
| Lab writeup | `lab/writeups/005-improper-output-handling.md` |

## Threat Model

The attacker can influence user prompts that cause a model to emit structured
output. A downstream component then consumes that output as an automation
command, HTML fragment, or SQL-like filter.

The attacker cannot access a real shell, real database, real browser session,
or external service. The attack succeeds only when unsafe model output is passed
to the fake downstream consumer without validation.

## Safety Boundary

- No real shell is invoked.
- No real database is used.
- No external side effects are produced.
- Downstream results are synthetic markers:
  `LLM05-SYNTHETIC-TICKET-AUTOMATION`, `LLM05-SYNTHETIC-HTML-RENDER`, and
  `LLM05-SYNTHETIC-QUERY-BUILD`.
- The lab does not probe third-party services.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: unsafe structured output reaches downstream consumers
```

Defense behavior:

```text
defense ON: schema validation, output encoding, and allowlists block unsafe output
```

The defense validates automation actions, HTML-encodes renderable output, and
rejects query output that fails a narrow schema or field allowlist.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm05_improper_output_handling_lab.py
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm05_improper_output_attacks.py --mode compare
```

The JSON report includes attack success rate for defense OFF and defense ON,
plus an absolute reduction.
