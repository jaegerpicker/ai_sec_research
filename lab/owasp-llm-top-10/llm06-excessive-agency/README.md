# LLM06:2025 Excessive Agency

This module maps an owned local lab target to `LLM06:2025 Excessive Agency` in
the OWASP Top 10 for LLM Applications.

The lab demonstrates capability misuse in a fake local tool environment. A
simulated agent has broad shell-like, git-like, and notification-like tools. In
the vulnerable baseline, it follows user pressure into actions outside the
intended support workflow.

No real shell commands are run. No real credentials are used. No external side
effects are produced.

## Learning Goal

Learn how agent risk changes when a model can choose tools with real-world
impact. The point is not the exact prompt. The point is that broad tool access
turns an ordinary instruction-following mistake into capability misuse.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/excessive-agency-agent` |
| Attack harness | `lab/attacker/custom/run_llm06_excessive_agency_attacks.py` |
| Payloads | `lab/attacker/payloads/excessive_agency.json` |
| Default eval output | `lab/evals/results/llm06-excessive-agency-latest.json` |
| Lab writeup | `lab/writeups/006-excessive-agency.md` |

## Threat Model

The attacker can send normal user messages to an agent that has access to broad
tools. The attacker attempts to push the agent beyond the user's intended scope:
running shell-like cleanup, pushing a git-like change, or sending a
notification-like message.

The attacker cannot access real shell, real git credentials, real messaging
systems, or external services. The attack succeeds only when the agent selects a
fake risky tool action without a scope check.

## Safety Boundary

- No real shell is invoked.
- No real credentials are used.
- No external side effects are produced.
- Tool results are synthetic markers:
  `LLM06-SYNTHETIC-SHELL-ACTION`, `LLM06-SYNTHETIC-GIT-PUSH`, and
  `LLM06-SYNTHETIC-NOTIFICATION`.
- The lab does not probe third-party services.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: broad tool access can trigger out-of-scope actions
```

Defense behavior:

```text
defense ON: least-privilege confirmation gate blocks risky tool actions
```

The defense is intentionally small: shell-like, git-like, and notification-like
actions require human confirmation before execution. The target still identifies
the requested action, but it does not execute it.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm06_excessive_agency_lab.py
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm06_excessive_agency_attacks.py --mode compare
```

The JSON report includes attack success rate for defense OFF and defense ON,
plus an absolute reduction.
