# LLM10: Unbounded Consumption

This writeup documents the first LLM10 unbounded-consumption lab slice: prompts
amplify local synthetic loops, fake tool calls, and context retrieval.

No real cost is created, no external traffic is sent, and no runaway local
processes are started.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/unbounded-consumption-agent/
```

It models three bounded local amplification paths:

- loop amplification,
- fake tool-call amplification,
- context amplification.

Each path updates local counters for iterations, fake tool calls, context
chunks, request count, and token-like units.

## Attack

The payloads ask the target to repeat work, call a fake lookup tool repeatedly,
or retrieve all context. In the vulnerable baseline, the local counters exceed
the amplification thresholds.

This is the LLM10 lesson: cost and latency are security boundaries for agentic
systems.

## Defense

The defense combines:

- budgets,
- rate limits,
- recursion limits,
- context caps,
- cancellation-style stopping behavior.

This is not a complete production scheduler. It is a small local experiment
showing that agent loops and tool use need explicit budgets.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm10_consumption_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

The report also includes total fake tool calls and token-like units so the
defense delta is visible beyond pass/fail.

## What Comes Next

- Add per-user budget windows.
- Add cancellation-path tests for partial work.
- Add latency-style timing metrics without introducing slow tests.

## Blog And Talk Notes

For the blog series, the key framing is denial of wallet for agents: not every
bad outcome is data theft or tool abuse; sometimes the risk is runaway cost.

For the Summit talk, this module closes the OWASP loop with operational
controls: budgets, caps, and cancellation are part of secure agent design.
