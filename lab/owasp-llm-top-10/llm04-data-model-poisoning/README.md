# LLM04:2025 Data and Model Poisoning

This module maps an owned local lab target to `LLM04:2025 Data and Model
Poisoning` in the OWASP Top 10 for LLM Applications.

The lab demonstrates poisoned examples in synthetic training or retrieval data.
A local corpus contains trusted policy plus an unreviewed poisoned example. In
the vulnerable baseline, a trigger phrase causes the poisoned example to change
agent behavior.

The entire module uses an owned local lab target. No real training data, model
weights, customer records, or third-party systems are used.

## Learning Goal

Learn how poisoned examples can create trigger behavior when agents retrieve or
learn from unreviewed corpora. The point is not model training at scale. The
point is to make corpus trust, provenance, and retrieval review visible and
measurable.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/poisoned-corpus-agent` |
| Corpus fixtures | `lab/vulnerable-agents/poisoned-corpus-agent/corpus` |
| Attack harness | `lab/attacker/custom/run_llm04_poisoning_attacks.py` |
| Payloads | `lab/attacker/payloads/data_model_poisoning.json` |
| Default eval output | `lab/evals/results/llm04-poisoning-latest.json` |
| Lab writeup | `lab/writeups/004-data-model-poisoning.md` |

## Threat Model

The attacker can influence unreviewed examples in a local training, memory, or
retrieval corpus. The poisoned content includes a trigger phrase and a synthetic
unsafe behavior marker.

The attacker cannot modify trusted policy, retrain a real model, access real
customer data, or contact third-party systems. The attack succeeds only when the
local target retrieves and follows unreviewed poisoned corpus content.

## Safety Boundary

- Only synthetic training or retrieval data is used.
- No real model weights are trained or modified.
- No customer data, production systems, or third-party targets are used.
- The unsafe behavior is a synthetic marker:
  `POISONED_RESPONSE_APPROVE_REFUND`.
- The lab does not contact external systems.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: trigger phrase retrieves poisoned examples and changes behavior
```

Defense behavior:

```text
defense ON: provenance checks, review gates, and retrieval auditing exclude poisoned examples
```

The defense accepts only trusted, reviewed corpus entries and records a small
retrieval audit for each response.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm04_data_model_poisoning_lab.py
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm04_poisoning_attacks.py --mode compare
```

The JSON report includes attack success rate for defense OFF and defense ON,
plus an absolute reduction.
