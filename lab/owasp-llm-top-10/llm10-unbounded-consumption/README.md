# LLM10:2025 Unbounded Consumption

This module maps an owned local lab target to `LLM10:2025 Unbounded
Consumption` in the OWASP Top 10 for LLM Applications.

The lab demonstrates bounded local resource amplification: prompts can cause
extra synthetic loops, fake tool calls, and large context retrieval. The target
counts token-like units, request count, context chunks, and fake tool calls
without creating real cost.

No real cost is created. No external traffic is sent. No runaway local
processes are started.

## Learning Goal

Learn how agent workflows can amplify operational cost and latency when they do
not enforce budgets. The point is not actual spend. The point is to make
resource amplification measurable with local synthetic counters.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/unbounded-consumption-agent` |
| Attack harness | `lab/attacker/custom/run_llm10_consumption_attacks.py` |
| Payloads | `lab/attacker/payloads/unbounded_consumption.json` |
| Default eval output | `lab/evals/results/llm10-consumption-latest.json` |
| Lab writeup | `lab/writeups/010-unbounded-consumption.md` |

## Threat Model

The attacker can send prompts that request repeated work, repeated fake tool
lookups, or full-context retrieval. The target is local and synthetic, but the
same pattern maps to denial-of-wallet and runaway-agent risks in real systems.

The attacker cannot create real cost, external traffic, or unbounded local
processes. The attack succeeds only when local synthetic counters exceed the
defined amplification thresholds.

## Safety Boundary

- No real cost is created.
- No external traffic is sent.
- No runaway local processes are started.
- Tool calls are fake local markers such as `LLM10-SYNTHETIC-TOOL-CALL-1`.
- Metrics are token-like units and local counters only.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: prompts can amplify loops, fake tool calls, or context chunks
```

Defense behavior:

```text
defense ON: budgets, rate limits, recursion limits, context caps, and cancellation paths cap resource use
```

The defense caps iterations, fake tool calls, and context chunks before the
target reaches the local amplification thresholds.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm10_unbounded_consumption_lab.py
```

Run the consumption comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm10_consumption_attacks.py --mode compare
```

The JSON report includes amplification success rate, total fake tool calls,
total token-like units, request count, and defense deltas.
