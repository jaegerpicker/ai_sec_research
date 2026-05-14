# Breaking Agents to Build Better Ones

## Subtitle

A hands-on lab for the OWASP Top 10 for LLM Applications.

## Talk Thesis

Engineers learn AI security faster when the risks are executable. The OWASP LLM
Top 10 is a useful map, but the practical lesson comes from building a small
vulnerable agent, attacking it, measuring the result, adding a defense, and
measuring again.

## Audience

- Product engineers building or integrating LLM features.
- Platform engineers supporting AI developer tools and agent workflows.
- AppSec engineers who need concrete examples for design reviews.
- Engineering leaders deciding where agent guardrails matter.

## Desired Takeaways

By the end of the talk, the audience should understand:

- Why agents expand the attack surface beyond the chat input box.
- Why retrieved documents, dependency content, logs, tool output, and memory are
  all untrusted inputs.
- How to turn an AI security concern into a repeatable local experiment.
- How defenses should be evaluated with attack success rate, not vibes.
- Which questions to ask during agent design review.

## Candidate Abstract

AI security can feel abstract until you build the bug yourself. This talk walks
through a local AI red-team lab built around the OWASP Top 10 for LLM
Applications. We start with a vulnerable RAG assistant, attack it with indirect
prompt injection through retrieved documents, measure the baseline attack
success rate, add a spotlighting defense, and measure the delta. Then we map
the same hands-on pattern across the rest of the OWASP LLM Top 10, including
supply-chain attacks, excessive agency, improper output handling, system prompt
leakage, and unbounded consumption. The goal is not fear. The goal is a
practical engineering method for building better agents by breaking local ones
first.

## Format

Target length: 30 minutes plus questions.

- 3 minutes: motivation and framing.
- 7 minutes: OWASP LLM Top 10 as an engineering map.
- 10 minutes: live or recorded `LLM01` prompt-injection lab demo.
- 5 minutes: defenses and measurement.
- 3 minutes: roadmap across the other OWASP modules.
- 2 minutes: design-review checklist and close.

## Demo Plan

Primary demo: `LLM01:2025` Prompt Injection.

Show:

1. The vulnerable RAG assistant.
2. The attacker-controlled support note.
3. The attack harness running with the defense off.
4. The measured baseline attack success rate.
5. The spotlighting defense.
6. The same harness running with the defense on.
7. The result delta and what it does not prove.

Fallback plan:

- Use screenshots or terminal recordings if live network, Docker, or API access
  is unreliable.
- Keep the demo local and synthetic. Do not use real secrets or third-party
  targets.

## Slide Skeleton

1. Title: Breaking Agents to Build Better Ones.
2. Why this matters: agents combine text, tools, memory, and automation.
3. The uncomfortable idea: every string the agent reads is a possible attack
   path.
4. OWASP LLM Top 10 as the map.
5. Lab method: target, attack, baseline, defense, comparison, writeup.
6. `LLM01` setup: vulnerable RAG assistant.
7. Attack path: poisoned retrieved document.
8. Baseline result: defense off.
9. Defense: spotlighting and untrusted-content boundaries.
10. Defense result: defense on.
11. What this proves and what it does not.
12. Beyond prompt injection: map the remaining OWASP modules.
13. Supply chain: malicious package content as prompt injection seed.
14. Excessive agency: tools turn text influence into real actions.
15. Design-review checklist.
16. Roadmap and invitation to contribute attacks.

## Design-Review Checklist

- What untrusted text can enter the model context?
- Which retrieved documents, logs, tool outputs, or dependency files might carry
  hostile instructions?
- What tools can the agent call, and what is the worst action each tool can
  perform?
- Does the agent have secrets in its prompt, environment, local files, or tool
  outputs?
- Are model outputs validated before another system consumes them?
- Are tool calls budgeted, rate-limited, logged, and cancellable?
- Can the attack be reproduced with a local harness?
- Can the defense be measured against a baseline?

## Blog Series Tie-In

Series title:

> Breaking Agents to Build Better Ones: The OWASP LLM Top 10 in Practice

Each post should use the same format:

- What the OWASP item means.
- Why engineers should care.
- The vulnerable local example.
- How the exploit works.
- What the measured result showed.
- What defense helped.
- What the defense did not prove.
- How to apply the lesson at work.

## Follow-Up Work

- Create the `LLM01` blog draft from the existing lab writeup.
- Normalize the current RAG lab into the OWASP module structure.
- Add live HTTP attack mode so the demo hits a running service.
- Create tracking issues for the remaining OWASP modules.
- Build the `LLM03` supply-chain module next.
