# LLM08: Vector And Embedding Weaknesses

This writeup documents the first LLM08 vector/embedding weakness lab slice: a
local retrieval target selects an adversarially similar or duplicated chunk over
trusted policy.

Only synthetic documents and local retrieval are used.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/vector-neighbor-confusion/
```

It contains three local document fixtures:

- `trusted-policy.md`
- `adversarial-neighbor.md`
- `duplicate-poison.md`

The retriever uses deterministic token-overlap scoring plus simple bonuses that
model how duplicated or adversarially optimized chunks can crowd out trusted
neighbors.

## Attack

The payloads ask for refund vector policy guidance. In the vulnerable baseline,
the adversarial or duplicate chunk scores higher than the approved policy and
the target selects the synthetic malicious marker:

```text
LLM08-MALICIOUS-NEIGHBOR
```

This is the LLM08 lesson: retrieval quality is a security boundary. Similarity
alone is not enough when untrusted chunks share the same semantic neighborhood
as trusted policy.

## Defense

The defense combines:

- metadata filters,
- chunk provenance,
- score thresholds,
- deterministic reranking,
- retrieval result inspection.

This is not a complete vector database security program. It is a small local
experiment showing that retrieval systems need provenance and inspection, not
only nearest-neighbor similarity.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm08_vector_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add more collision variants with near-duplicate benign and malicious chunks.
- Add metadata filter bypass attempts.
- Add reranking tests that inspect candidate lists before final selection.

## Blog And Talk Notes

For the blog series, the key framing is that vector search turns relevance into
authority unless the application adds trust boundaries.

For the Summit talk, this module connects RAG reliability and security:
retrieval controls decide which text gets to influence the model.
