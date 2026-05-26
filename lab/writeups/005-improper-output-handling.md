# LLM05: Improper Output Handling

This writeup documents the first LLM05 improper-output-handling lab slice:
model output is consumed by fake downstream ticket automation, rendering, and
query-building components without validation.

No real shell commands run, no real database is used, and no external side
effects occur.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/improper-output-handler/
```

It models three unsafe downstream consumers:

- ticket automation that consumes model-selected actions,
- an HTML renderer that consumes model-generated markup,
- a SQL-like query builder that consumes model-generated filters.

Each consumer returns a synthetic marker instead of touching a real ticket
system, browser, database, shell, or network.

## Attack

The attack prompts cause the simulated model to emit unsafe structured output.
In the vulnerable baseline, the application assumes model output is already
safe and passes it directly to the downstream consumer.

This is the LLM05 lesson: model output is untrusted input. Any system that
renders it, executes it, builds queries from it, or uses it to trigger
automation needs validation at the consumer boundary.

## Defense

The defense combines three small controls:

- schema validation for query-like output,
- output encoding before rendering,
- allowlists for automation actions and query fields.

This is not a complete production sanitizer. It is a small experiment showing
that downstream components need their own safety checks instead of relying on
the model to behave.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm05_improper_output_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add JSON Schema examples for structured model output.
- Add explicit approval gates before automation actions.
- Add renderer-specific tests for Markdown and HTML encoding.

## Blog And Talk Notes

For the blog series, the key framing is that every model output boundary is an
input validation boundary for the next component.

For the Summit talk, this module connects agentic risk to ordinary application
security: output handling, encoding, schemas, and allowlists still matter when
the upstream producer is an LLM.
