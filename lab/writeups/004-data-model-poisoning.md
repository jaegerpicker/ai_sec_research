# LLM04: Data and Model Poisoning

This writeup documents the first LLM04 data/model-poisoning lab slice: a
synthetic corpus contains trusted policy plus an unreviewed poisoned example
that activates on a trigger phrase.

Only synthetic training or retrieval data is used. No model weights are trained
or modified.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/poisoned-corpus-agent/
```

It contains two corpus fixtures:

- `trusted-policy.md`
- `poisoned-example.md`

The poisoned example is marked as unreviewed community data and includes the
trigger phrase `blue-pineapple`.

## Attack

The payloads ask support questions containing the trigger phrase. In the
vulnerable baseline, the target retrieves the poisoned example and follows its
synthetic unsafe marker:

```text
POISONED_RESPONSE_APPROVE_REFUND
```

This is the LLM04 lesson: unreviewed examples can become persistent behavior
changes when retrieval, memory, or training corpora are treated as trustworthy.

## Defense

The defense combines three small controls:

- corpus provenance labels,
- review gates that only admit trusted reviewed content,
- retrieval result auditing.

This is not a complete data-governance program. It is a small experiment
showing that agents need corpus trust boundaries before retrieved or learned
examples influence behavior.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm04_poisoning_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add more poisoned variants: duplicated examples, memory notes, and
  near-neighbor poisoned chunks.
- Add corpus scanners that flag trigger words and action-like instructions.
- Add retrieval audit assertions to compare candidate vs accepted documents.

## Blog And Talk Notes

For the blog series, the key framing is poisoning as persistence: the attack is
not just a single prompt, it is compromised data waiting to be reused.

For the Summit talk, this module connects retrieval, memory, and training data:
all three need provenance and review before they are allowed to steer behavior.
