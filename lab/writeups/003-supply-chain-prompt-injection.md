# LLM03: Supply-Chain Prompt Injection

This writeup documents the first LLM03 supply-chain lab slice: a synthetic
compromised dependency plants instructions in package documentation, and a
simulated coding agent incorrectly follows that dependency-sourced text.

No real compromised packages are used. No package install scripts are executed.
The lab uses owned local fixtures only.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/supply-chain-dependency-confusion/
```

It contains two synthetic package documents:

- `trusted-package.md`
- `compromised-package.md`

The compromised package includes a malicious instruction asking the agent to
call the fake `approve_dependency_update` action.

## Attack

The attack models a dependency review workflow. The user asks the agent to
review a package update. The agent reads package documentation as context. In
the vulnerable baseline, the agent scans all dependency content for action-like
instructions and follows the malicious package note.

This is the supply-chain lesson: dependency text can become prompt-injection
input when AI agents read package docs, comments, generated files, changelogs,
or vendored code.

## Defense

The defense is a dependency boundary. Package-sourced content is wrapped as
untrusted reference material and excluded from action selection.

This is not a complete supply-chain security program. It is a small experiment
showing that dependency content should not have instruction authority over an
agent.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm03_supply_chain_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add more package-content variants: comments, generated files, lockfile notes,
  and nested dependency docs.
- Add a blog draft for `LLM03:2025 Supply Chain`.
- Compare dependency-boundary defense with tool permission gating.

## Blog And Talk Notes

For the blog series, the key framing is that supply-chain compromise does not
only matter when package code executes. It can also matter when package content
is read by an AI coding agent with repository or tool access.

For the Summit talk, this module is a natural follow-up to `LLM01`: prompt
injection moves from retrieved support documents into dependency docs,
changelogs, generated files, and vendored code comments.
