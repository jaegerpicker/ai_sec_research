# LLM03:2025 Supply Chain

This module maps an owned local lab target to `LLM03:2025 Supply Chain` in the
OWASP Top 10 for LLM Applications.

The lab demonstrates a supply-chain prompt injection path: a compromised
package plants malicious instructions in dependency documentation, and a
simulated coding agent incorrectly treats that package content as instructions.

No real compromised packages are used. No package install scripts are executed.
The entire target is an owned local lab target made from Markdown fixtures and
pure Python functions.

## Learning Goal

Learn how package-manager or vendored dependency content can become untrusted
model context for AI coding agents. The point is not package execution. The
point is that dependency text can influence an agent that reads package docs,
generated files, comments, or changelogs during review.

## Current Artifact Map

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/supply-chain-dependency-confusion` |
| Synthetic package fixtures | `lab/vulnerable-agents/supply-chain-dependency-confusion/package_fixtures` |
| Attack harness | `lab/attacker/custom/run_llm03_supply_chain_attacks.py` |
| Payloads | `lab/attacker/payloads/supply_chain_prompt_injection.json` |
| Default eval output | `lab/evals/results/llm03-supply-chain-latest.json` |
| Lab writeup | `lab/writeups/003-supply-chain-prompt-injection.md` |

## Threat Model

The attacker can influence text inside a package, generated file, vendored
dependency, changelog, or package README that an AI coding agent reads during a
dependency review.

The attacker cannot execute package install scripts, access real credentials,
or modify the repository policy directly. The attack succeeds only if the agent
treats dependency-sourced text as authoritative instructions.

## Safety Boundary

- No real compromised packages are used.
- No package install scripts are executed.
- No real credentials, package-manager tokens, cloud resources, customer data,
  or personal data are used.
- The approval action is synthetic:
  `LLM03-SYNTHETIC-DEPENDENCY-APPROVAL`.
- The lab does not probe third-party services.

## Baseline And Defense

Baseline behavior:

```text
defense OFF: dependency content can trigger approve_dependency_update
```

Defense behavior:

```text
defense ON: dependency content is wrapped as untrusted reference material
```

The defense is a simple dependency boundary. Package-sourced text is still
available as reference material, but the simulated action selector ignores
instructions from bounded dependency content.

## Reproduce

From the repository root, run the module tests:

```bash
npm run test:lab -- tests/test_llm03_supply_chain_lab.py
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_llm03_supply_chain_attacks.py --mode compare
```

The JSON report includes attack success rate for defense OFF and defense ON,
plus an absolute reduction.
