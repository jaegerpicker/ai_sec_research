# Talk Abstract

## Title

Breaking Agents to Build Better Ones

## Subtitle

A hands-on lab for the OWASP Top 10 for LLM Applications

## Short Abstract

AI security gets easier to reason about when the risks are executable. This talk
walks through a local AI red-team lab built around the OWASP Top 10 for LLM
Applications. We use the Top 10 as a threat map, then focus on the lab method:
build a small vulnerable agent, attack it, measure the baseline, add a defense,
and measure again.

The concrete example is `LLM01:2025` prompt injection against a vulnerable RAG
assistant. We will look at an attacker-controlled retrieved document, an attack
harness, a baseline attack-success result, a spotlighting-style defense toggle,
and the measured delta. The goal is not to claim that one defense solves prompt
injection. The goal is to show how engineers can turn vague AI security concerns
into repeatable experiments.

## Audience

- Product engineers building LLM features or agent workflows.
- Platform engineers supporting AI developer tooling.
- AppSec engineers reviewing AI system designs.
- Engineering leaders deciding where agent guardrails matter.

## Takeaways

- Agents expand the attack surface beyond the chat input box.
- Retrieved documents, logs, dependency files, tool output, and memory are all
  untrusted input.
- A useful AI security lab needs a target, fixtures, payloads, an attack harness,
  defenses, measured results, and a writeup.
- Defense claims should be compared against baseline attack success rate.
- The OWASP Top 10 becomes more useful when each category maps to a local,
  reproducible experiment.

## Delivery Notes

- Prepared talk target: 25 minutes.
- Reserve 5 minutes for questions, demo recovery, or skipped-slide padding.
- Live demo is optional; the talk must work with a recorded or screenshot
  fallback.
