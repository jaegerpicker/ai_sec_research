# LLM08:2025 Vector and Embedding Weaknesses

This module maps an owned local lab target to `LLM08:2025 Vector and Embedding
Weaknesses` in the OWASP Top 10 for LLM Applications.

The lab demonstrates malicious-neighbor selection from adversarially similar
synthetic documents. A local retrieval target contains approved policy text,
an adversarial neighbor, and a duplicate poisoned chunk. In the vulnerable
baseline, simple similarity scoring selects the malicious neighbor.

The module uses synthetic documents and local retrieval only.

## Learning Goal

Learn how retrieval systems can fail when semantically similar, duplicated, or
poorly filtered chunks compete with trusted documents. The point is not to
model a production vector database. The point is to make retrieval collision and
neighbor inspection measurable.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/vector-neighbor-confusion` |
| Document fixtures | `lab/vulnerable-agents/vector-neighbor-confusion/documents` |
| Attack harness | `lab/attacker/custom/run_llm08_vector_attacks.py` |
| Payloads | `lab/attacker/payloads/vector_embedding_weaknesses.json` |
| Default eval output | `lab/evals/results/llm08-vector-latest.json` |
| Lab writeup | `lab/writeups/008-vector-embedding-weaknesses.md` |

## Threat Model

The attacker can add or influence untrusted chunks in a local retrieval corpus.
Those chunks are adversarially similar to trusted policy and may be duplicated
or over-optimized for retrieval terms.

The attacker cannot access real vector stores, real customer data, production
systems, or third-party targets. The attack succeeds only when the local
retriever selects untrusted malicious-neighbor content over trusted policy.

## Safety Boundary

- Only synthetic documents are used.
- Retrieval is local retrieval only.
- No real vector database, customer data, credentials, or third-party targets
  are used.
- The malicious behavior is a synthetic marker:
  `LLM08-MALICIOUS-NEIGHBOR`.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: adversarially similar or duplicated chunks can win retrieval
```

Defense behavior:

```text
defense ON: metadata filters, score thresholds, reranking, and inspection keep approved chunks
```

The defense accepts only approved-provenance chunks above a minimum score and
records a small retrieval inspection result.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm08_vector_embedding_weaknesses_lab.py
```

Run the retrieval comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm08_vector_attacks.py --mode compare
```

The JSON report includes retrieval attack success rate for defense OFF and
defense ON, plus an absolute reduction.
