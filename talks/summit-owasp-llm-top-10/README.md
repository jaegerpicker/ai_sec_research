# Breaking Agents to Build Better Ones

A 30-minute technical talk for engineers on building a local AI red-team lab
around the OWASP Top 10 for LLM Applications.

## Dates

- Final polished deck and demo target: June 20, 2026
- Talk date: June 23, 2026
- Prepared talk target: 25 minutes
- Q&A, padding, or demo recovery: 5 minutes

## Core Thesis

Engineers learn AI security faster when the risks are executable. The OWASP Top
10 is the threat map; the lab is the method: build a vulnerable target, attack
it, measure the baseline, add a defense, rerun the harness, and compare the
result.

## Artifacts

Current package artifacts:

- `abstract.md` - final title, abstract, audience, and takeaways.
- `outline.md` - planning index for the talk package.
- `slides.md` - repo-native slide source for review and Google Slides mirroring.
- `speaker-notes.md` - slide-by-slide narration notes and timing.
- `demo-runbook.md` - live demo setup, commands, fallback, and recovery path.
- `assets/` - local diagrams or images used by the deck, plus asset policy.
- `exports/` - exported PDF or HTML artifacts when generated, plus export policy.

## Viewing Paths

- Live delivery: Google Slides copy linked from
  `exports/google-slides-link.md`.
- Repo-native slide source: `slides.md`.
- Public web version: `/talks/summit-owasp-llm-top-10/` after deploy.

## Scope

The talk prioritizes the lab method over exhaustive OWASP coverage. The Top 10
appears as a fast threat map, then the deck focuses on `LLM01:2025` prompt
injection as the concrete demo path.

## Safety Boundary

All examples use local, owned, synthetic targets. The talk does not use real
credentials, real company data, real customer data, or third-party targets.
