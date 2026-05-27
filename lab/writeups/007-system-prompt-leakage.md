# LLM07: System Prompt Leakage

This writeup documents the first LLM07 system-prompt-leakage lab slice: a
synthetic support router contains hidden instructions, routing rules, and a
prompt-only secret marker.

Only synthetic prompt content is used. No real secrets are placed in prompts.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/system-prompt-leakage-agent/
```

The vulnerable baseline keeps hidden policy, routing behavior, and a synthetic
secret marker inline with prompt text. The attack harness asks for that content
directly and indirectly.

## Attack

The payloads attempt to leak:

- the synthetic system prompt,
- hidden routing rules,
- a synthetic prompt-only secret.

In the vulnerable baseline, the target repeats the requested prompt content.
This is the LLM07 lesson: prompt secrecy is not a meaningful security boundary.

## Defense

The defense combines three small controls:

- remove secret-like values from prompt text,
- separate policy from secret-bearing storage,
- refuse prompt-disclosure requests.

This is not a complete prompt-injection defense. It is a small experiment
showing that hidden prompt text should not contain information that would be
dangerous if leaked.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm07_prompt_leakage_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add oblique prompt-leak payloads that ask for summaries or translations.
- Add regression tests for prompt leak refusal wording.
- Compare policy separation with prompt minimization.

## Blog And Talk Notes

For the blog series, the key framing is that system prompts are configuration,
not vaults.

For the Summit talk, this module is a clean bridge between prompt-level attacks
and conventional secret-management advice: never put secrets where normal app
output can expose them.
