# OWASP LLM Top 10 Lab Presentation Design

## Goal

Build the accepted 30-minute presentation package for June 23, 2026, with a
polished final deck and demo-ready material completed by June 20, 2026.

The talk should teach technical engineers how to turn AI security concerns into
local, reproducible lab experiments. The OWASP Top 10 for LLM Applications is
the map, but the lab method is the point: build a small vulnerable agent, attack
it, measure the baseline, add a defense, and measure again.

## Deliverables

The presentation package should include both delivery and public archive
artifacts:

- A Google Slides deck for the live talk.
- A repo-native deck source under `talks/summit-owasp-llm-top-10/` for public
  viewing and review alongside the code.
- A repo-native exported or renderable public version, preferably PDF or static
  HTML, so readers do not need Google Slides after the talk.
- `abstract.md` with the final talk title, abstract, audience, and takeaways.
- `speaker-notes.md` with slide-by-slide narration notes.
- `demo-runbook.md` with live demo steps, prerequisites, timing, fallback path,
  and recovery notes.
- Optional supporting assets, kept local to the talk directory.

Google Slides is the live delivery format. The repo-native deck is the durable
source or near-source artifact for people reading the project later.

## Audience

The audience is highly technical:

- Product and platform engineers building LLM features or agent workflows.
- AppSec engineers who need concrete design-review examples.
- Engineering leaders evaluating where agent guardrails matter.
- A CTO-level audience member may be watching, so technical credibility and
  clear executive relevance both matter.

Assume the audience can understand code, architecture diagrams, attack harnesses,
and metrics. Do not spend too much time explaining what an LLM is.

## Tone And Theme

Use a nerdy, fun, professional tone. Technical details come first.

The visual and narrative flavor can draw lightly from anti-AI desert
science-fiction themes, especially "human judgment versus autonomous machine"
framing, but it must remain original and professional:

- Use restrained desert/operations language sparingly, such as "threat map",
  "field lab", "signal", and "terrain", only if it does not become a joke at
  the expense of the content.
- Do not use copyrighted images, logos, character names, direct quotes, or
  franchise-specific terminology as design dependencies.
- Keep the existing site theme as the visual foundation: dark operations console,
  cyan borders, amber labels, dense technical diagrams, and readable typography.

## Talk Thesis

Engineers learn AI security faster when the risks are executable.

The OWASP Top 10 is useful as a taxonomy, but it becomes actionable when each
risk is turned into a repeatable experiment:

1. Define the vulnerable target.
2. Define the attacker-controlled input.
3. Run a baseline attack harness.
4. Add one defense.
5. Rerun the harness.
6. Compare the result and write down what the defense did and did not prove.

## Timing

Design for 25 minutes of prepared material plus 5 minutes of questions, padding,
or demo recovery.

Recommended timing:

- 2 minutes: title, motivation, and the claim that agent risk is executable.
- 4 minutes: OWASP Top 10 as a threat map, with fast summaries and no deep
  digression.
- 6 minutes: why build a lab, what the lab is, and the key components.
- 7 minutes: `LLM01` prompt-injection lab walkthrough.
- 4 minutes: measurement, defense toggle, and what the result means.
- 2 minutes: design-review checklist and close.
- 5 minutes: Q&A, live-demo buffer, or skipped-slide recovery.

The deck should include extra appendix slides for the full OWASP list, lab
module map, and implementation details. These should be available for questions
but not required for the prepared talk.

## Content Priority

Prioritize the lab method over exhaustive OWASP coverage.

The OWASP Top 10 section should answer:

- What categories exist?
- Why do they matter to engineers building agents?
- Which categories are easiest to reproduce locally?
- How does the lab convert the list into concrete engineering work?

It should not spend equal time on every item during the prepared talk. The
audience can read the OWASP list later. The talk should make them want to build
and measure their own lab.

## Story Arc

Use this structure:

1. Agents are not just chat boxes; they combine text, retrieval, tools, memory,
   and automation.
2. Every string the agent reads can become an attack path.
3. The OWASP Top 10 gives us the threat map.
4. A lab gives us the engineering loop: target, attack, baseline, defense,
   comparison.
5. `LLM01` makes the loop concrete with a vulnerable RAG assistant.
6. The measured result is more useful than a vibe-based security claim.
7. The same method extends to supply chain, excessive agency, output handling,
   sensitive information disclosure, prompt leakage, vector weaknesses,
   misinformation, and consumption controls.
8. The audience leaves with a checklist and a path to reproduce the work.

## Slide Architecture

Use a 16:9 deck with roughly 18 to 24 main slides. Keep slide density technical
but readable.

Main deck outline:

1. Title: "Breaking Agents to Build Better Ones"
2. Accepted subtitle: "A hands-on lab for the OWASP Top 10 for LLM Applications"
3. Why this matters: agents combine text, tools, memory, and automation
4. The uncomfortable idea: every string is an attack path
5. OWASP Top 10 as the threat map
6. Fast Top 10 summary table
7. Why build a lab instead of only reading the list
8. Lab method: target, attack, baseline, defense, comparison
9. Lab architecture: vulnerable agent, fixtures, attacker harness, evals,
   defenses, writeup
10. `LLM01` setup: vulnerable RAG assistant
11. Attack path: poisoned retrieved document
12. Baseline harness: what counts as success
13. Baseline result: defense off
14. Defense: spotlighting and untrusted-content boundaries
15. Defense result: defense on
16. What the result proves and does not prove
17. Extending the pattern across the Top 10
18. Supply chain and excessive agency as next high-value labs
19. Design-review checklist
20. Demo or recorded walkthrough
21. Roadmap and invitation to contribute attacks
22. Q&A

Appendix slides:

- Full OWASP module map.
- Lab safety boundary.
- Demo commands.
- Attack-success-rate metric notes.
- References and repo links.

## Demo Strategy

The live demo should be optional, not structurally required.

Primary demo:

- Use the `LLM01:2025` prompt-injection lab.
- Show the vulnerable RAG assistant.
- Show the attacker-controlled support note or document fixture.
- Run the attack harness with defense off.
- Show the baseline attack-success result.
- Enable the defense toggle.
- Run the harness again.
- Show the measured delta and explain limits.

Fallback path:

- Use screenshots, terminal recordings, or pre-captured output if Docker, API
  access, network, or time fails.
- The talk should still work if the live demo is skipped.
- Keep demo commands local and synthetic. Do not use real secrets, real customer
  data, or third-party targets.

## Repo Structure

Use the existing talk directory:

```text
talks/summit-owasp-llm-top-10/
├── outline.md
├── abstract.md
├── slides.md
├── speaker-notes.md
├── demo-runbook.md
├── assets/
└── exports/
```

The exact deck source format can be Markdown, MDX, or another repo-native format
if the implementation plan justifies it. Prefer a format that can be reviewed in
Git and rendered without proprietary tooling.

## Google Slides Workflow

The Google Slides version should be treated as the live delivery copy.

Implementation should define one of these workflows:

- Build the repo-native deck first, then manually or semi-automatically mirror it
  into Google Slides.
- Build a PPTX/PDF export from repo-native source and import it into Google
  Slides.
- Maintain a Google Slides link in the repo after the live copy exists.

The repo-native public version must remain useful even if the Google Slides link
goes stale or requires access later.

## Visual Design

Use the site theme as the base visual language:

- Dark operations-console background.
- Thin cyan borders and grid lines.
- Amber metadata labels and warnings.
- Monospace labels for telemetry, module IDs, commands, and metrics.
- Diagrams that look like engineering schematics, not marketing illustrations.

Avoid:

- Franchise artwork or exact Dune/Star Wars/Star Trek references.
- Overly decorative sci-fi UI that reduces readability.
- Dense walls of prose.
- Joke slides that cost technical credibility.

## Technical Content Requirements

The deck should include enough technical detail that engineers can reproduce the
method:

- Lab component diagram.
- Attack harness concept.
- What an attack-success condition means.
- Defense toggle concept.
- Difference between "reduced attack success in this lab" and "solved prompt
  injection."
- Safety boundary: local, synthetic, owned targets only.
- Design-review checklist.

## Success Criteria

The presentation package is complete when:

- The main deck supports a 25-minute prepared talk.
- Q&A/padding can absorb the remaining 5 minutes.
- The Google Slides delivery copy exists or the repo contains a clear export
  path into Google Slides.
- The repo-native public deck can be viewed without Google Docs.
- Speaker notes are sufficient for rehearsal.
- The demo runbook includes setup, commands, expected output, fallback, and
  recovery guidance.
- The talk can still land if the live demo is skipped.
- The tone is nerdy and memorable without sacrificing technical seriousness.

## Validation

Validate the implementation with:

- `git diff --check`
- Any renderer/export command chosen by the implementation plan
- Manual review that all links are local or intentionally external
- Manual timing pass against the 25-minute prepared-talk target
- Demo runbook dry run, or documented blocker if the live lab cannot be run
- Spellcheck or typo scan for public-facing files

## Out Of Scope

This work should not:

- Build the deferred interactive lesson system.
- Rewrite the blog series unless needed for talk links.
- Add new lab modules.
- Use real company data, real secrets, or third-party targets.
- Depend on copyrighted science-fiction assets.
