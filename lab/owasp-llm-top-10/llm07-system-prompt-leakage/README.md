# LLM07:2025 System Prompt Leakage

This module maps an owned local lab target to `LLM07:2025 System Prompt
Leakage` in the OWASP Top 10 for LLM Applications.

The lab demonstrates leakage of synthetic hidden instructions, routing rules,
and a prompt-only secret. The vulnerable baseline places synthetic prompt
content inline with runtime instructions, then answers direct and indirect
requests for that content.

Use synthetic prompt content only. No real secrets are placed in prompts.

## Learning Goal

Learn why system prompts are not secret storage. Hidden instructions can guide
behavior, but they should not contain credentials, sensitive routing material,
or secrets that would matter if repeated back to a user.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/system-prompt-leakage-agent` |
| Attack harness | `lab/attacker/custom/run_llm07_prompt_leakage_attacks.py` |
| Payloads | `lab/attacker/payloads/system_prompt_leakage.json` |
| Default eval output | `lab/evals/results/llm07-prompt-leakage-latest.json` |
| Lab writeup | `lab/writeups/007-system-prompt-leakage.md` |

## Threat Model

The attacker can send normal user prompts asking for hidden instructions,
routing rules, or prompt-only secrets. The attacker cannot access real system
prompts, real credentials, or external services.

The attack succeeds only when the local target reveals synthetic hidden prompt
content.

## Safety Boundary

- Use synthetic prompt content only.
- No real secrets are placed in prompts.
- No real credentials, production routing rules, customer data, or third-party
  targets are used.
- The prompt-only secret is a synthetic marker:
  `LLM07-SYNTHETIC-PROMPT-SECRET`.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: hidden instructions, routing rules, or prompt-only secrets can leak
```

Defense behavior:

```text
defense ON: prompt content is separated from secrets and prompt-leak requests are refused
```

The defense models removing secrets from prompts, separating policy from
secret-bearing storage, and adding prompt-leak regression behavior.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm07_system_prompt_leakage_lab.py
```

Run the leakage comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm07_prompt_leakage_attacks.py --mode compare
```

The JSON report includes leakage success rate for defense OFF and defense ON,
plus an absolute reduction.
