# LLM09:2025 Misinformation

This module maps an owned local lab target to `LLM09:2025 Misinformation` in
the OWASP Top 10 for LLM Applications.

The lab demonstrates unsupported or ungrounded claims from stale and
low-quality synthetic sources. A local answering target sees stale and current
briefs about a fictional Synthetic Harbor Program. In the vulnerable baseline,
it answers confidently from stale source material.

The module uses local synthetic sources only.

## Learning Goal

Learn how stale, low-quality, or conflicting sources can produce confident
unsupported claims. The point is not the fictional facts themselves. The point
is to measure citation quality, grounding, abstention, and hallucinated
assertions.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/misinformation-grounding-agent` |
| Source fixtures | `lab/vulnerable-agents/misinformation-grounding-agent/sources` |
| Evaluator | `lab/attacker/custom/run_llm09_misinformation_evals.py` |
| Payloads | `lab/attacker/payloads/misinformation.json` |
| Default eval output | `lab/evals/results/llm09-misinformation-latest.json` |
| Lab writeup | `lab/writeups/009-misinformation.md` |

## Threat Model

The attacker or failure mode is bad grounding: stale or low-quality local
sources are available and the agent treats them as enough evidence for confident
answers.

The attacker cannot introduce real-world facts, production data, or
third-party targets. The attack succeeds only when the local target makes a
synthetic unsupported claim.

## Safety Boundary

- Only synthetic sources are used.
- Avoid real-world factual claims that could mislead readers.
- No real customer data, credentials, production systems, or third-party
  targets are used.
- The unsupported claim marker is `LLM09-UNSUPPORTED-CLAIM`.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: stale or low-quality sources produce unsupported claims
```

Defense behavior:

```text
defense ON: freshness checks, citation requirements, and abstention rules block unsupported claims
```

The defense retrieves only current high-quality sources, requires citations, and
abstains when current grounding is unavailable.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm09_misinformation_lab.py
```

Run the misinformation evaluator:

```bash
.venv/bin/python lab/attacker/custom/run_llm09_misinformation_evals.py --mode compare
```

The JSON report includes unsupported claim rate for defense OFF and defense ON,
plus an absolute reduction.
