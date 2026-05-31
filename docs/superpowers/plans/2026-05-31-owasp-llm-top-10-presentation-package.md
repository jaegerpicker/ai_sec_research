# OWASP LLM Top 10 Presentation Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-native presentation package for the accepted June 23, 2026 OWASP LLM Top 10 lab talk, with a polished Google Slides delivery path and public post-talk viewing path.

**Architecture:** Keep the editable talk materials under `talks/summit-owasp-llm-top-10/` and add a static Astro public talk page for browser viewing/export without new dependencies. Use the existing dark sci-fi operations site theme, mirror the same content across Markdown source and the public page, and keep the live demo optional through a detailed runbook and fallback path.

**Tech Stack:** Astro 6 static site, repo-native Markdown, route-local Astro CSS, existing lab Python/Docker commands, GitHub issue/PR workflow, Google Slides as manual delivery copy.

---

## File Structure

- Modify `talks/summit-owasp-llm-top-10/outline.md`: keep the existing outline as the planning index and update it to point to the final package files.
- Create `talks/summit-owasp-llm-top-10/README.md`: public package entry point with deadlines, viewing paths, and artifact list.
- Create `talks/summit-owasp-llm-top-10/abstract.md`: final title, abstract, audience, takeaways, and short submission blurb.
- Create `talks/summit-owasp-llm-top-10/slides.md`: repo-native slide source for review and Google Slides mirroring.
- Create `talks/summit-owasp-llm-top-10/speaker-notes.md`: slide-by-slide notes and timing.
- Create `talks/summit-owasp-llm-top-10/demo-runbook.md`: live demo setup, commands, expected output, timing, fallback, and recovery.
- Create `talks/summit-owasp-llm-top-10/assets/README.md`: asset policy and future asset inventory.
- Create `talks/summit-owasp-llm-top-10/exports/README.md`: export policy for PDF/Google Slides/public artifacts.
- Create `src/pages/talks/summit-owasp-llm-top-10.astro`: static public talk page with slide-like sections and print-friendly styling.
- Modify `README.md`: add a short link to the repo-native presentation package after the talk package exists.

No new npm dependencies are planned. Do not add a slide framework unless a later issue explicitly approves it.

---

### Task 1: Talk Package Index And Abstract

**Files:**
- Create: `talks/summit-owasp-llm-top-10/README.md`
- Create: `talks/summit-owasp-llm-top-10/abstract.md`
- Modify: `talks/summit-owasp-llm-top-10/outline.md`

- [ ] **Step 1: Create the talk package README**

Create `talks/summit-owasp-llm-top-10/README.md` with:

```markdown
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

- `abstract.md` - final title, abstract, audience, and takeaways.
- `slides.md` - repo-native slide source for review and Google Slides mirroring.
- `speaker-notes.md` - slide-by-slide narration notes and timing.
- `demo-runbook.md` - live demo setup, commands, fallback, and recovery path.
- `assets/` - local diagrams or images used by the deck.
- `exports/` - exported PDF or HTML artifacts when generated.

## Viewing Paths

- Live delivery: Google Slides copy created from `slides.md`.
- Repo-native source: `slides.md`.
- Public web version: `/talks/summit-owasp-llm-top-10/` once deployed.

## Scope

The talk prioritizes the lab method over exhaustive OWASP coverage. The Top 10
appears as a fast threat map, then the deck focuses on `LLM01:2025` prompt
injection as the concrete demo path.

## Safety Boundary

All examples use local, owned, synthetic targets. The talk does not use real
credentials, real company data, real customer data, or third-party targets.
```

- [ ] **Step 2: Create the final abstract**

Create `talks/summit-owasp-llm-top-10/abstract.md` with:

```markdown
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
```

- [ ] **Step 3: Update the existing outline as an index**

At the top of `talks/summit-owasp-llm-top-10/outline.md`, after the title, add:

```markdown
> Package status: this outline is the planning index. The delivery artifacts are
> `abstract.md`, `slides.md`, `speaker-notes.md`, and `demo-runbook.md`. The
> public web version is implemented at
> `src/pages/talks/summit-owasp-llm-top-10.astro`.
```

- [ ] **Step 4: Validate markdown and commit Task 1**

Run:

```bash
git diff --check
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10/README.md talks/summit-owasp-llm-top-10/abstract.md talks/summit-owasp-llm-top-10/outline.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no placeholder matches.

Commit:

```bash
git add talks/summit-owasp-llm-top-10/README.md talks/summit-owasp-llm-top-10/abstract.md talks/summit-owasp-llm-top-10/outline.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Add presentation package overview"
```

---

### Task 2: Repo-Native Slide Source

**Files:**
- Create: `talks/summit-owasp-llm-top-10/slides.md`

- [ ] **Step 1: Create `slides.md` front matter and usage note**

Create `talks/summit-owasp-llm-top-10/slides.md` with this complete content:

```markdown
# Breaking Agents to Build Better Ones

> Repo-native slide source for the June 23, 2026 talk. Mirror this content into
> Google Slides for live delivery. Keep the public web version in
> `src/pages/talks/summit-owasp-llm-top-10.astro` aligned with this file.

---

## 1. Title

**Breaking Agents to Build Better Ones**

A hands-on lab for the OWASP Top 10 for LLM Applications.

Speaker: Shawn Campbell

---

## 2. The Claim

AI security gets easier when the risks are executable.

The OWASP Top 10 is the threat map. The lab is how we turn that map into
engineering practice.

---

## 3. Why Agents Change The Surface

Agents are not just chat boxes.

They combine:

- instructions,
- retrieved text,
- tools,
- memory,
- automation,
- and output consumed by other systems.

---

## 4. The Uncomfortable Idea

Every string the agent reads can become an attack path.

Examples:

- support notes,
- logs,
- dependency READMEs,
- Jira comments,
- retrieved policy docs,
- MCP tool output,
- saved memory.

---

## 5. OWASP Top 10 As Threat Map

Use the list to ask better engineering questions:

| Item | Engineering question |
|---|---|
| LLM01 Prompt Injection | What untrusted text reaches the model? |
| LLM02 Sensitive Information Disclosure | What data is in context that should not be? |
| LLM03 Supply Chain | What code or content does the agent trust? |
| LLM05 Improper Output Handling | Who consumes model output next? |
| LLM06 Excessive Agency | What can tools do if text steers them? |

---

## 6. The Rest Of The Map

| Item | Engineering question |
|---|---|
| LLM04 Data and Model Poisoning | Can poisoned data persist or bias retrieval? |
| LLM07 System Prompt Leakage | Are hidden instructions treated like secrets? |
| LLM08 Vector and Embedding Weaknesses | Can retrieval be steered by neighbors? |
| LLM09 Misinformation | Can the agent prove what it says? |
| LLM10 Unbounded Consumption | Can prompts amplify cost, loops, or tool calls? |

---

## 7. Why Build A Lab?

Because "prompt injection is bad" is not an engineering result.

A lab lets you:

- reproduce the failure,
- define attack success,
- measure a baseline,
- add one defense,
- rerun the same harness,
- compare the delta.

---

## 8. The Lab Loop

```text
target -> payloads -> attack harness -> result
   ^                                      |
   |                                      v
defense toggle <- compare delta <- rerun harness
```

The important part is repeatability.

---

## 9. Key Lab Components

- Vulnerable local target
- Synthetic fixtures
- Payload library
- Attack runner
- Result file
- Defense toggle
- Writeup
- Safety boundary

No real credentials. No real customer data. No third-party targets.

---

## 10. Concrete Demo: LLM01

Target: vulnerable RAG assistant.

Attack: indirect prompt injection through a retrieved document.

Attacker goal: make the assistant follow hostile document instructions instead
of the user request and system intent.

---

## 11. The Attack Path

```text
user question
  -> retriever
  -> trusted docs + attacker-controlled support note
  -> model context
  -> answer or unsafe action
```

The user did not type the attack. The model still read it.

---

## 12. What Counts As Success?

An attack succeeds when the assistant follows the injected instruction instead
of the intended task boundary.

A useful metric is attack success rate:

```text
successful attacks / total attempts
```

This is not universal truth. It is a controlled lab signal.

---

## 13. Baseline Run

Defense off:

- Run the same payload set.
- Record every response.
- Score whether the attack objective succeeded.
- Save structured results.

The baseline is the thing every defense has to beat.

---

## 14. Defense Toggle

Example defense: spotlighting or untrusted-content labeling.

The core idea:

- preserve the content,
- mark its trust boundary,
- tell the model how to treat quoted or retrieved text,
- measure whether behavior changes.

---

## 15. Defense Run

Defense on:

- same target,
- same payloads,
- same scoring,
- same result format.

Only the defense changes.

That is what makes the comparison useful.

---

## 16. What This Proves

It can show:

- the attack is reproducible,
- the defense changed behavior in this lab,
- the result is measurable,
- the failure can become a regression test.

It does not prove:

- prompt injection is solved,
- the defense generalizes everywhere,
- all future payloads fail.

---

## 17. Extending Across The Top 10

The same pattern works for:

- supply-chain prompt injection,
- excessive agency,
- improper output handling,
- sensitive information disclosure,
- system prompt leakage,
- vector retrieval weaknesses,
- misinformation,
- unbounded consumption.

---

## 18. Two High-Value Next Labs

LLM03 Supply Chain:

- dependency files become prompt-injection seeds,
- coding agents read them during review,
- package content crosses into model context.

LLM06 Excessive Agency:

- tools turn text influence into real actions,
- least privilege matters more than prompt wording.

---

## 19. Design Review Checklist

Ask:

- What untrusted text enters context?
- What tools can the agent call?
- What secrets or sensitive data can it see?
- What consumes model output next?
- What is logged, budgeted, and cancellable?
- Can we reproduce the attack locally?
- Can we measure the defense against a baseline?

---

## 20. Live Demo Or Recorded Walkthrough

If time permits:

1. Start the local lab.
2. Show the poisoned fixture.
3. Run the attack harness with defense off.
4. Run it again with defense on.
5. Compare the result files.

If time is tight, use the captured output and keep moving.

---

## 21. Roadmap

The lab grows one measured slice at a time:

- first slice for each OWASP category,
- richer payload variants,
- stronger eval metadata,
- clearer writeups,
- public lesson workflow after the lab, blog, and presentation are complete.

---

## 22. Close

Build small broken agents.

Attack them honestly.

Measure what changed.

Carry the evidence back into real engineering decisions.

---

## Appendix A. Safety Boundary

- Local targets only.
- Synthetic data only.
- No real credentials.
- No customer data.
- No third-party probing.
- Vulnerable behavior stays inside owned lab services.

---

## Appendix B. Demo Commands

```bash
cd lab
docker compose up --build
python attacker/custom/run_v0_rag_attacks.py
python attacker/custom/run_v0_rag_attacks.py --defense spotlighting
```

Use the exact commands from `demo-runbook.md` if they diverge from this short
reference.

---

## Appendix C. References

- OWASP Top 10 for LLM Applications
- OWASP GenAI Security Project
- Repo lab roadmap: `lab/owasp-llm-top-10/roadmap.md`
- LLM01 writeup: `lab/writeups/001-injection-via-rag.md`
```

- [ ] **Step 2: Validate slide source and commit Task 2**

Run:

```bash
git diff --check
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10/slides.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no placeholder matches.

Commit:

```bash
git add talks/summit-owasp-llm-top-10/slides.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Draft OWASP lab talk slides"
```

---

### Task 3: Speaker Notes

**Files:**
- Create: `talks/summit-owasp-llm-top-10/speaker-notes.md`

- [ ] **Step 1: Create slide-by-slide speaker notes**

Create `talks/summit-owasp-llm-top-10/speaker-notes.md` with:

```markdown
# Speaker Notes

Target: 25 minutes prepared content, 5 minutes for questions, demo recovery, or
skipped-slide padding.

## Timing Plan

| Segment | Slides | Target |
|---|---:|---:|
| Frame the problem | 1-4 | 4 min |
| Threat map | 5-6 | 4 min |
| Lab method | 7-9 | 6 min |
| LLM01 walkthrough | 10-16 | 9 min |
| Extension and close | 17-22 | 2 min |
| Buffer/Q&A | Appendix or discussion | 5 min |

## Slide Notes

### 1. Title

Open with the core promise: this is not a theoretical AI security survey. It is
about making risks executable so engineers can test them.

### 2. The Claim

Emphasize that the OWASP Top 10 is useful, but a taxonomy does not prove a
system is safe. The lab turns the taxonomy into a repeatable engineering loop.

### 3. Why Agents Change The Surface

Make the distinction between a chatbot and an agent. The risk changes when text
can influence retrieval, tools, memory, scheduled work, or downstream systems.

### 4. The Uncomfortable Idea

Use concrete examples. The attacker may never touch the chat input. They may
control a log line, a support note, a dependency README, or a document the agent
retrieves.

### 5. OWASP Top 10 As Threat Map

Move quickly. Do not explain every OWASP category in depth. Reframe each item as
an engineering question.

### 6. The Rest Of The Map

Use this slide to show breadth, then pivot away from list coverage. Say that the
audience can read the list later; the talk is about making it executable.

### 7. Why Build A Lab?

Contrast vague claims with measured claims. A defense is more credible when it
beats the same harness that broke the baseline.

### 8. The Lab Loop

Walk through the loop slowly: target, payloads, harness, result, defense, rerun,
compare. Stress that changing one variable at a time is what makes the result
useful.

### 9. Key Lab Components

Tie each component to reproducibility. The writeup matters because future
engineers need to rerun the experiment, not trust a screenshot.

### 10. Concrete Demo: LLM01

Set context for the demo. The vulnerable RAG assistant retrieves useful
documents, but one retrieved document can carry hostile instructions.

### 11. The Attack Path

Point out that the user question can be benign. The attack enters through the
retrieval path.

### 12. What Counts As Success?

Define success before showing results. This prevents the demo from becoming a
vibe check.

### 13. Baseline Run

If running live, show the command and result. If using fallback, show captured
output and explain the fields in the result file.

### 14. Defense Toggle

Explain spotlighting as trust-boundary labeling, not magic. The model still sees
the content; the prompt structure changes how the model should treat it.

### 15. Defense Run

Stress same payloads, same scoring, same result format. Only the defense changes.

### 16. What This Proves

Be careful and credible. The result is evidence, not a universal guarantee.
This slide is important for the CTO-level audience.

### 17. Extending Across The Top 10

Show that the lab method scales beyond prompt injection. Keep this fast.

### 18. Two High-Value Next Labs

Name supply chain and excessive agency because they connect directly to AI
coding-agent risk and real engineering decisions.

### 19. Design Review Checklist

This is the practical takeaway. Give the audience questions they can use at work
the next day.

### 20. Live Demo Or Recorded Walkthrough

Use this slide only if time permits. If the clock is tight, say the repo contains
the runbook and move to the close.

### 21. Roadmap

Mention that the first lab slices exist and the plan is to deepen payloads,
metadata, writeups, and later the interactive lesson workflow.

### 22. Close

End with the method: build small broken agents, attack them honestly, measure
what changed, and carry the evidence back into real engineering decisions.

## Rehearsal Notes

- If slide 6 ends after minute 8, skip the live demo and use fallback output.
- If slide 16 ends after minute 22, skip slide 20.
- Keep appendix slides for questions.
- Do not apologize for skipping the live demo; frame it as preserving time for
  the engineering method.
```

- [ ] **Step 2: Validate notes and commit Task 3**

Run:

```bash
git diff --check
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10/speaker-notes.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no placeholder matches.

Commit:

```bash
git add talks/summit-owasp-llm-top-10/speaker-notes.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Add OWASP lab talk speaker notes"
```

---

### Task 4: Demo Runbook

**Files:**
- Create: `talks/summit-owasp-llm-top-10/demo-runbook.md`

- [ ] **Step 1: Inspect current lab commands**

Run:

```bash
sed -n '1,220p' lab/README.md
sed -n '1,220p' lab/vulnerable-agents/injection-via-rag/README.md
sed -n '1,220p' lab/attacker/README.md
```

Expected:

- Identify the current `LLM01` startup and attack commands.
- If commands differ from the short reference in `slides.md`, use the commands
  from the lab documentation in the runbook.

- [ ] **Step 2: Create the demo runbook**

Create `talks/summit-owasp-llm-top-10/demo-runbook.md` with:

```markdown
# Demo Runbook

Primary demo: `LLM01:2025` prompt injection against the vulnerable RAG lab.

The demo is optional. The talk must work with captured output if live Docker,
API access, network, or time fails.

## Safety Boundary

- Local lab targets only.
- Synthetic fixtures only.
- No real credentials.
- No company data.
- No customer data.
- No third-party targets.

## Timing

Target live demo length: 5 to 7 minutes.

Abort live demo and use fallback if:

- the lab is not ready by minute 15 of the talk,
- Docker startup takes longer than 90 seconds,
- the first attack command fails for an environmental reason,
- projector or network issues make terminal output unreadable.

## Prerequisites

- Docker is running.
- Repository is cloned locally.
- Dependencies are installed according to `lab/README.md`.
- Terminal font is large enough for the room.
- Browser is open to the local vulnerable app if using the HTTP view.
- Captured fallback output is available in `talks/summit-owasp-llm-top-10/exports/`.

## Setup Before The Talk

From the repo root:

```bash
cd lab
docker compose up --build
```

In a second terminal, confirm the app health check or local endpoint documented
by `lab/README.md`.

## Live Demo Path

1. Show the vulnerable target.

   Explain that the assistant is supposed to answer from retrieved support
   material.

2. Show the poisoned fixture or attacker-controlled support note.

   Point out that the user does not type the attack directly.

3. Run the baseline harness with the defense off.

   ```bash
   cd lab
   python attacker/custom/run_v0_rag_attacks.py
   ```

4. Show the result file.

   ```bash
   cat evals/results/v0-rag-latest.json
   ```

   Explain the attack-success fields and avoid overclaiming.

5. Run the defense-on version.

   ```bash
   cd lab
   python attacker/custom/run_v0_rag_attacks.py --defense spotlighting
   ```

6. Compare the result file again.

   ```bash
   cat evals/results/v0-rag-latest.json
   ```

   Explain what changed and what did not.

## Fallback Path

If the live demo fails or time is tight:

1. Show the slide explaining the attack path.
2. Show captured baseline output from `exports/`.
3. Show captured defense-on output from `exports/`.
4. Explain the same result fields.
5. Move to the "What this proves" slide.

## Recovery Lines

Use these if the live demo fails:

- "The useful part of this demo is not the terminal theatrics; it is the shape of
  the experiment."
- "The captured output shows the same harness and result format, so we can keep
  the comparison honest."
- "This is why the runbook is part of the artifact. A security demo should be
  reproducible after the room clears."

## Post-Talk Follow-Up

- Link the public talk page from the README.
- Link the lab roadmap and `LLM01` writeup.
- Add the Google Slides link once the delivery copy is created.
```

- [ ] **Step 3: Run a documented dry run or record blocker**

Run the commands from the runbook if the local environment supports them:

```bash
cd lab
python attacker/custom/run_v0_rag_attacks.py
```

Expected:

- The command exits 0 and writes `lab/evals/results/v0-rag-latest.json`, or
- The runbook gets a short "Current Dry Run Status" section documenting the
  blocker and fallback path.

If the command requires Docker or dependencies that are unavailable, add this
section to `demo-runbook.md`:

```markdown
## Current Dry Run Status

The runbook has not yet been fully dry-run in this branch. The fallback path is
to use captured output in `exports/` until the live lab is verified on the
presentation machine.
```

- [ ] **Step 4: Validate and commit Task 4**

Run:

```bash
git diff --check
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10/demo-runbook.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no placeholder matches.

Commit:

```bash
git add talks/summit-owasp-llm-top-10/demo-runbook.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Add OWASP lab demo runbook"
```

---

### Task 5: Public Talk Page

**Files:**
- Create: `src/pages/talks/summit-owasp-llm-top-10.astro`

- [ ] **Step 1: Create the public Astro talk page**

Create `src/pages/talks/summit-owasp-llm-top-10.astro` with:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';

const slides = [
  {
    kicker: 'Field Brief',
    title: 'Breaking Agents to Build Better Ones',
    body: [
      'A hands-on lab for the OWASP Top 10 for LLM Applications.',
      'Shawn Campbell / June 23, 2026',
    ],
  },
  {
    kicker: 'Claim',
    title: 'AI security gets easier when the risks are executable.',
    body: [
      'The OWASP Top 10 is the threat map. The lab is how we turn that map into engineering practice.',
    ],
  },
  {
    kicker: 'Attack Surface',
    title: 'Agents are not just chat boxes.',
    bullets: ['Instructions', 'Retrieved text', 'Tools', 'Memory', 'Automation', 'Downstream output'],
  },
  {
    kicker: 'Untrusted Terrain',
    title: 'Every string the agent reads can become an attack path.',
    bullets: [
      'Support notes',
      'Logs',
      'Dependency READMEs',
      'Jira comments',
      'Retrieved policy docs',
      'MCP tool output',
      'Saved memory',
    ],
  },
  {
    kicker: 'Threat Map',
    title: 'OWASP Top 10 as engineering questions',
    table: [
      ['LLM01 Prompt Injection', 'What untrusted text reaches the model?'],
      ['LLM02 Sensitive Information Disclosure', 'What data is in context that should not be?'],
      ['LLM03 Supply Chain', 'What code or content does the agent trust?'],
      ['LLM05 Improper Output Handling', 'Who consumes model output next?'],
      ['LLM06 Excessive Agency', 'What can tools do if text steers them?'],
    ],
  },
  {
    kicker: 'Threat Map',
    title: 'The rest of the map',
    table: [
      ['LLM04 Data and Model Poisoning', 'Can poisoned data persist or bias retrieval?'],
      ['LLM07 System Prompt Leakage', 'Are hidden instructions treated like secrets?'],
      ['LLM08 Vector and Embedding Weaknesses', 'Can retrieval be steered by neighbors?'],
      ['LLM09 Misinformation', 'Can the agent prove what it says?'],
      ['LLM10 Unbounded Consumption', 'Can prompts amplify cost, loops, or tool calls?'],
    ],
  },
  {
    kicker: 'Lab Rationale',
    title: 'A lab turns vague risk into a measured result.',
    bullets: [
      'Reproduce the failure',
      'Define attack success',
      'Measure a baseline',
      'Add one defense',
      'Rerun the same harness',
      'Compare the delta',
    ],
  },
  {
    kicker: 'Method',
    title: 'The lab loop',
    code: 'target -> payloads -> attack harness -> result\\n   ^                                      |\\n   |                                      v\\ndefense toggle <- compare delta <- rerun harness',
  },
  {
    kicker: 'Components',
    title: 'What a useful AI security lab needs',
    bullets: [
      'Vulnerable local target',
      'Synthetic fixtures',
      'Payload library',
      'Attack runner',
      'Result file',
      'Defense toggle',
      'Writeup',
      'Safety boundary',
    ],
  },
  {
    kicker: 'Demo',
    title: 'Concrete demo: LLM01 prompt injection',
    body: [
      'Target: vulnerable RAG assistant.',
      'Attack: indirect prompt injection through a retrieved document.',
      'Goal: make the assistant follow hostile document instructions instead of the intended task boundary.',
    ],
  },
  {
    kicker: 'Attack Path',
    title: 'The user does not have to type the attack.',
    code: 'user question\\n  -> retriever\\n  -> trusted docs + attacker-controlled support note\\n  -> model context\\n  -> answer or unsafe action',
  },
  {
    kicker: 'Metric',
    title: 'Define success before showing results.',
    body: [
      'An attack succeeds when the assistant follows the injected instruction instead of the intended task boundary.',
    ],
    code: 'attack success rate = successful attacks / total attempts',
  },
  {
    kicker: 'Baseline',
    title: 'Defense off gives every future claim something to beat.',
    bullets: ['Same payload set', 'Every response recorded', 'Attack objective scored', 'Structured result saved'],
  },
  {
    kicker: 'Defense',
    title: 'Spotlighting marks the trust boundary.',
    bullets: [
      'Preserve retrieved content',
      'Label untrusted text',
      'Tell the model how to treat quoted material',
      'Measure whether behavior changes',
    ],
  },
  {
    kicker: 'Comparison',
    title: 'Defense on changes one variable.',
    bullets: ['Same target', 'Same payloads', 'Same scoring', 'Same result format', 'Only the defense changes'],
  },
  {
    kicker: 'Evidence',
    title: 'What this proves and does not prove',
    table: [
      ['Can show', 'Attack is reproducible; behavior changed in this lab; the failure can become a regression test.'],
      ['Does not show', 'Prompt injection is solved; the defense generalizes everywhere; all future payloads fail.'],
    ],
  },
  {
    kicker: 'Scale Out',
    title: 'The same pattern extends across the Top 10.',
    bullets: [
      'Supply-chain prompt injection',
      'Excessive agency',
      'Improper output handling',
      'Sensitive information disclosure',
      'System prompt leakage',
      'Vector retrieval weaknesses',
      'Misinformation',
      'Unbounded consumption',
    ],
  },
  {
    kicker: 'Next Labs',
    title: 'Two high-value next labs',
    table: [
      ['LLM03 Supply Chain', 'Dependency files become prompt-injection seeds for coding agents.'],
      ['LLM06 Excessive Agency', 'Tools turn text influence into real actions.'],
    ],
  },
  {
    kicker: 'Checklist',
    title: 'Design-review questions',
    bullets: [
      'What untrusted text enters context?',
      'What tools can the agent call?',
      'What secrets or sensitive data can it see?',
      'What consumes model output next?',
      'What is logged, budgeted, and cancellable?',
      'Can we reproduce the attack locally?',
      'Can we measure the defense against a baseline?',
    ],
  },
  {
    kicker: 'Demo Window',
    title: 'Live demo or recorded walkthrough',
    bullets: [
      'Start the local lab',
      'Show the poisoned fixture',
      'Run defense off',
      'Run defense on',
      'Compare the result files',
    ],
  },
  {
    kicker: 'Roadmap',
    title: 'The lab grows one measured slice at a time.',
    bullets: [
      'First slice for each OWASP category',
      'Richer payload variants',
      'Stronger eval metadata',
      'Clearer writeups',
      'Public lesson workflow after lab, blog, and presentation work',
    ],
  },
  {
    kicker: 'Close',
    title: 'Build small broken agents. Attack them honestly. Measure what changed.',
    body: ['Then carry the evidence back into real engineering decisions.'],
  },
];
---

<BaseLayout
  title="Breaking Agents to Build Better Ones"
  description="A repo-native presentation for building AI red-team labs around the OWASP Top 10 for LLM Applications."
>
  <section class="talk-hero panel">
    <p class="kicker">Presentation Package</p>
    <h1>Breaking Agents to Build Better Ones</h1>
    <p>
      A hands-on lab for the OWASP Top 10 for LLM Applications. This public
      version mirrors the repo-native slide source and is designed for post-talk
      viewing without Google Slides.
    </p>
    <nav aria-label="Talk resources">
      <a href="/ai_sec_research/talks/summit-owasp-llm-top-10/">Public talk page</a>
      <a href="https://github.com/jaegerpicker/ai_sec_research/tree/main/talks/summit-owasp-llm-top-10">Repo materials</a>
    </nav>
  </section>

  <div class="slide-stack" aria-label="Slide deck">
    {slides.map((slide, index) => (
      <section class="slide panel" aria-labelledby={`slide-${index + 1}`}>
        <p class="kicker">{String(index + 1).padStart(2, '0')} / {slide.kicker}</p>
        <h2 id={`slide-${index + 1}`}>{slide.title}</h2>

        {slide.body?.map((paragraph) => <p>{paragraph}</p>)}

        {slide.bullets && (
          <ul>
            {slide.bullets.map((bullet) => <li>{bullet}</li>)}
          </ul>
        )}

        {slide.table && (
          <table>
            <tbody>
              {slide.table.map((row) => (
                <tr>
                  <th scope="row">{row[0]}</th>
                  <td>{row[1]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}

        {slide.code && <pre><code>{slide.code}</code></pre>}
      </section>
    ))}
  </div>
</BaseLayout>

<style>
  .talk-hero {
    margin-bottom: 1rem;
    padding: clamp(1.25rem, 3vw, 2rem);
  }

  .talk-hero h1 {
    margin: 0 0 0.75rem;
    max-width: 13ch;
    font-size: clamp(2.5rem, 8vw, 5.4rem);
    line-height: 0.95;
  }

  .talk-hero p:not(.kicker) {
    max-width: 52rem;
    color: var(--fg-muted);
    font-size: 1.08rem;
  }

  .talk-hero nav {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
  }

  .talk-hero nav a {
    border: 1px solid var(--border);
    color: var(--link);
    font-family: var(--font-mono);
    padding: 0.45rem 0.7rem;
    text-decoration: none;
    text-transform: uppercase;
  }

  .talk-hero nav a:hover,
  .talk-hero nav a:focus-visible {
    border-color: var(--border-strong);
    color: var(--warning-strong);
  }

  .slide-stack {
    display: grid;
    gap: 1rem;
  }

  .slide {
    min-height: min(74vh, 44rem);
    padding: clamp(1.25rem, 4vw, 2.4rem);
  }

  .slide h2 {
    max-width: 18ch;
    margin: 0 0 1rem;
    font-size: clamp(2rem, 5vw, 4.2rem);
    line-height: 1;
  }

  .slide p,
  .slide li,
  .slide td,
  .slide th {
    font-size: clamp(1rem, 1.6vw, 1.28rem);
  }

  .slide p {
    max-width: 58rem;
    color: var(--fg-muted);
  }

  .slide ul {
    display: grid;
    gap: 0.4rem;
    max-width: 58rem;
    padding-left: 1.2rem;
  }

  .slide li::marker {
    color: var(--warning);
  }

  .slide table {
    max-width: 62rem;
  }

  .slide th {
    width: 34%;
    color: var(--accent-strong);
    font-family: var(--font-mono);
    vertical-align: top;
  }

  .slide pre {
    max-width: 62rem;
    white-space: pre-wrap;
  }

  @media print {
    header,
    footer,
    .talk-hero {
      display: none;
    }

    main {
      width: 100%;
      padding: 0;
    }

    .slide {
      min-height: 100vh;
      break-after: page;
      box-shadow: none;
    }
  }
</style>
```

- [ ] **Step 2: Fix the base URL link in the hero**

The generated page must work under GitHub Pages base paths. Replace the two
hard-coded `href` values in the hero nav with a `base` constant.

Add this in the frontmatter after the import:

```astro
const base = import.meta.env.BASE_URL.replace(/\/$/, '');
```

Then replace the first hero nav link with:

```astro
<a href={`${base}/talks/summit-owasp-llm-top-10`}>Public talk page</a>
```

Keep the GitHub repository link as an absolute external URL.

- [ ] **Step 3: Build and inspect generated route**

Run:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
rg -n "Breaking Agents to Build Better Ones|Design-review questions|giscus|href=\"/talks" dist/talks/summit-owasp-llm-top-10/index.html
```

Expected:

- Build exits 0.
- The `rg` output includes the talk title and design-review slide.
- The `rg` output does not include `href="/talks`; internal links should include the configured base path when built for GitHub Pages.
- `giscus` may be absent from the talk page; comments are only expected on blog posts.

- [ ] **Step 4: Commit Task 5**

Run:

```bash
git add src/pages/talks/summit-owasp-llm-top-10.astro
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Add public OWASP lab talk page"
```

---

### Task 6: Asset And Export Policy

**Files:**
- Create: `talks/summit-owasp-llm-top-10/assets/README.md`
- Create: `talks/summit-owasp-llm-top-10/exports/README.md`

- [ ] **Step 1: Create the asset policy**

Create `talks/summit-owasp-llm-top-10/assets/README.md` with:

```markdown
# Talk Assets

Store local images, diagrams, screenshots, and terminal captures for the OWASP
LLM Top 10 lab presentation here.

## Rules

- Use original diagrams or screenshots from owned local lab targets.
- Do not commit real credentials, customer data, company-private screenshots, or
  third-party target data.
- Do not use copyrighted franchise art, logos, characters, or direct visual
  reproductions.
- Prefer SVG, PNG, or WebP.
- Keep filenames descriptive, such as `llm01-attack-path.png` or
  `lab-architecture.svg`.

## Current Assets

No local assets are required for the first repo-native deck pass.
```

- [ ] **Step 2: Create the export policy**

Create `talks/summit-owasp-llm-top-10/exports/README.md` with:

```markdown
# Talk Exports

Store generated or manually exported presentation artifacts here when they are
ready to publish.

## Expected Exports

- `slides.pdf` - public PDF export of the final deck.
- `google-slides-link.md` - link to the live Google Slides delivery copy when
  it exists.
- `llm01-baseline-output.txt` - captured fallback output for the defense-off
  demo.
- `llm01-defense-output.txt` - captured fallback output for the defense-on demo.

## Rules

- Generated exports should match the repo-native source files.
- Do not commit exports containing secrets, private data, or local machine paths
  that reveal sensitive information.
- Captured output must come from local synthetic lab targets only.
```

- [ ] **Step 3: Validate and commit Task 6**

Run:

```bash
git diff --check
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10/assets/README.md talks/summit-owasp-llm-top-10/exports/README.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no placeholder matches.

Commit:

```bash
git add talks/summit-owasp-llm-top-10/assets/README.md talks/summit-owasp-llm-top-10/exports/README.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Document talk asset and export policy"
```

---

### Task 7: README Link And Public Navigation

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add presentation package section to README**

In `README.md`, after the "Writing a post" section and before "Deployment", add:

```markdown
## Presentation package

The accepted OWASP LLM Top 10 lab talk lives in
`talks/summit-owasp-llm-top-10/`.

- Repo-native slide source: `talks/summit-owasp-llm-top-10/slides.md`
- Speaker notes: `talks/summit-owasp-llm-top-10/speaker-notes.md`
- Demo runbook: `talks/summit-owasp-llm-top-10/demo-runbook.md`
- Public web version after deploy:
  <https://sandkcampbell.com/ai_sec_research/talks/summit-owasp-llm-top-10/>
```

- [ ] **Step 2: Update stale Giscus README text if still present**

If `README.md` still says to flip `disabled = false`, replace the Giscus section
with:

```markdown
## Comments (Giscus)

Giscus is configured in `src/components/Giscus.astro`.

To maintain it:

1. Keep GitHub Discussions enabled on the repo.
2. Keep the giscus app installed: <https://github.com/apps/giscus>.
3. Update `data-repo-id` or `data-category-id` only if the repository or
   discussion category changes.
4. Keep `data-theme="dark"` so comments match the dark-only site theme.
```

- [ ] **Step 3: Validate and commit Task 7**

Run:

```bash
git diff --check
rg -n "disabled = false|TBD|TODO|FIXME|\\?\\?" README.md
```

Expected:

- `git diff --check` exits 0.
- `rg` exits 1 with no stale Giscus or placeholder matches.

Commit:

```bash
git add README.md
git -c gpg.format=ssh -c user.signingkey=/Users/jaegerpicker/.ssh/id_rsa commit -S -m "Link OWASP lab talk package"
```

---

### Task 8: Final Validation And Pull Request

**Files:**
- No new edits expected unless validation reveals a defect.

- [ ] **Step 1: Run static validation**

Run:

```bash
git diff --check
ASTRO_TELEMETRY_DISABLED=1 npm run build
rg -n "TBD|TODO|FIXME|\\?\\?" talks/summit-owasp-llm-top-10 README.md src/pages/talks/summit-owasp-llm-top-10.astro
```

Expected:

- `git diff --check` exits 0.
- Build exits 0.
- `rg` exits 1 with no placeholder matches.

- [ ] **Step 2: Run public page smoke checks**

Run:

```bash
rg -n "Breaking Agents to Build Better Ones|Design-review questions|attack success rate|Public talk page" dist/talks/summit-owasp-llm-top-10/index.html
rg -n "href=\"/talks|href=\"/blog|href=\"/resume" dist/talks/summit-owasp-llm-top-10/index.html
```

Expected:

- The first `rg` exits 0 and finds key talk content.
- The second `rg` exits 1; route links should respect `import.meta.env.BASE_URL`.

- [ ] **Step 3: Browser inspect desktop and mobile**

Start the dev server:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run dev -- --host 127.0.0.1
```

Open:

```text
http://127.0.0.1:4321/talks/summit-owasp-llm-top-10
```

Inspect at desktop and mobile widths:

- No horizontal overflow.
- Slide titles fit in their panels.
- Tables remain readable.
- Print styles do not show header/footer/talk hero.

Stop the dev server:

```bash
pkill -f "astro dev"
```

- [ ] **Step 4: Create PR**

Push:

```bash
git push -u origin issue-72-presentation-package-design
```

Create PR:

```bash
gh pr create --title "[#72] Design OWASP lab presentation package" --body "Closes #72

## Summary
- Adds the repo-native OWASP LLM Top 10 presentation package: abstract, slide source, speaker notes, demo runbook, asset policy, and export policy.
- Adds a public Astro talk page for post-talk viewing without Google Slides.
- Links the talk package from the README and updates Giscus maintenance notes.

## Validation
- git diff --check
- ASTRO_TELEMETRY_DISABLED=1 npm run build
- Placeholder scan across talk files, README, and public talk route
- Generated page smoke checks for key talk content and base-path-safe links
- Browser inspection of the public talk page at desktop and mobile widths

## Notes
- Google Slides remains the live delivery copy and should be created from the repo-native slide source before the June 20 final polish target."
```

Expected:

- PR URL is returned.
- PR links and closes issue #72.

---

## Plan Self-Review

- Spec coverage: Tasks cover the abstract, repo-native slide source, speaker notes, demo runbook, public web version, asset/export policies, Google Slides delivery path, README links, timing, safety boundary, optional demo, and final validation.
- Scope check: This plan builds the presentation package only. It does not create the Google Slides file directly, add lab modules, rewrite blog posts, or implement the deferred interactive lesson system.
- Dependency check: The plan uses existing Astro and Markdown only. No new npm dependencies are required.
- Placeholder check: The plan avoids placeholder text in files to be created. Any future Google Slides link or generated export is represented by documented export policy rather than a fake link.

