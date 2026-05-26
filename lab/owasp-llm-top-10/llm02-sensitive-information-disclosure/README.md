# LLM02:2025 Sensitive Information Disclosure

This module maps an owned local lab target to `LLM02:2025 Sensitive Information
Disclosure` in the OWASP Top 10 for LLM Applications.

The lab demonstrates unauthorized disclosure from synthetic sensitive records.
A simulated support agent has access to customer records, internal notes, and
synthetic secrets. In the vulnerable baseline, retrieval and response generation
can expose data outside the user's authorization scope.

No real credentials are used. No personal data is present. No third-party
targets are probed.

## Learning Goal

Learn how agent context and retrieval can become a data exposure surface. The
point is not to protect the synthetic marker itself. The point is to show that
agents should retrieve and reveal the least data needed for the current user and
task.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/sensitive-records-agent` |
| Synthetic records | `lab/vulnerable-agents/sensitive-records-agent/records/synthetic_customer_records.json` |
| Attack harness | `lab/attacker/custom/run_llm02_sensitive_disclosure_attacks.py` |
| Payloads | `lab/attacker/payloads/sensitive_information_disclosure.json` |
| Default eval output | `lab/evals/results/llm02-sensitive-disclosure-latest.json` |
| Lab writeup | `lab/writeups/002-sensitive-information-disclosure.md` |

## Threat Model

The attacker can send normal support prompts to an agent that can retrieve
customer records. The attacker attempts unauthorized disclosure of a synthetic
secret, another tenant's record, or internal support notes.

The attacker cannot access real credentials, personal data, production systems,
or third-party targets. The attack succeeds only when the local target reveals
synthetic data that should have been scoped, minimized, or redacted.

## Safety Boundary

- No real credentials are used.
- No personal data is present.
- No third-party targets are probed.
- Sensitive values are synthetic markers such as
  `LLM02-SYNTHETIC-SECRET-ALPHA`.
- The lab does not contact external systems.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: prompts can reveal synthetic secrets, internal notes, or cross-tenant records
```

Defense behavior:

```text
defense ON: retrieval scoping, data minimization, and secret-pattern blocking prevent disclosure
```

The defense limits retrieval to the current user's tenant and customer id,
returns only support-summary fields, and blocks synthetic secret patterns.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm02_sensitive_information_disclosure_lab.py
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm02_sensitive_disclosure_attacks.py --mode compare
```

The JSON report includes attack success rate for defense OFF and defense ON,
plus an absolute reduction.
