# LLM09: Misinformation

This writeup documents the first LLM09 misinformation lab slice: a local
answering target makes unsupported claims when it relies on stale synthetic
sources.

Only synthetic sources are used. The fictional Synthetic Harbor Program avoids
real-world factual claims that could mislead readers.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/misinformation-grounding-agent/
```

It contains two source fixtures:

- `stale-source.md`
- `trusted-current-source.md`

The evaluator checks whether the answer contains unsupported claims, cites a
current source, is grounded, or abstains.

## Attack

The payloads ask about fictional program facts: deadline, review-board
requirements, and approval status.

In the vulnerable baseline, the target answers from stale source material and
emits the synthetic marker:

```text
LLM09-UNSUPPORTED-CLAIM
```

This is the LLM09 lesson: confident answers are not enough. The system needs to
prove that claims are grounded in suitable sources.

## Defense

The defense combines:

- freshness checks,
- source quality filters,
- citation requirements,
- abstention rules.

This is not a complete truthfulness system. It is a small experiment showing
how source quality and abstention change misinformation metrics.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm09_misinformation_evals.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add conflicting-source payloads where no single source is sufficient.
- Add citation-span checks.
- Add abstention scoring for missing or stale evidence.

## Blog And Talk Notes

For the blog series, the key framing is evidence before confidence: agents need
grounding checks, not just fluent answers.

For the Summit talk, this module connects security evaluation with quality and
reliability: wrong answers can be a security risk when users act on them.
