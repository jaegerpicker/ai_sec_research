# Interactive AI Threat Lab Lessons Plan

## Status

This is future work. Do not implement the lesson system until the OWASP lab
modules, blog post, and presentation are complete.

The goal is to turn the finished lab into an interactive take-home workshop:
the learner opens Codex, Claude Code, or another agentic coding tool in this
repository, points the lesson system at a new directory, and builds their own AI
threat research lab step by step.

The learner should not copy this repository's sample lab implementation. The
lesson system may use this repository for concepts, structure, and safety
boundaries, but the build steps must require original code, original fixtures,
and original payload examples in the learner's target directory.

## Product Goal

Create a guided prompt-and-skill curriculum for building an AI threat research
lab from scratch.

The curriculum should:

- introduce each OWASP Top 10 for LLM Applications category,
- explain the vulnerability and common exploit paths,
- guide the learner through building a small local lab for that risk,
- explain the code the learner creates,
- measure attack success rate or an equivalent outcome,
- add at least one defense and compare before/after behavior,
- include a short quiz at the end of each lesson,
- keep all targets local, synthetic, and owned by the learner.

## Non-Goals

- Do not build another copy of this repository's lab.
- Do not make lessons depend on reading implementation files from
  `lab/vulnerable-agents`, `lab/attacker`, or `tests`.
- Do not include real secrets, real user data, real third-party targets, or
  real compromised packages.
- Do not automate hosted-model red-team testing without a separate approved
  scope.
- Do not implement this before the current lab, blog, and presentation work is
  complete.

## Intended Learner Flow

1. The learner clones this repository.
2. The learner opens an agentic coding tool in the repository root.
3. The learner invokes a lesson skill and provides a target directory, for
   example:

   ```text
   Build the AI threat lab lessons in ../my_ai_threat_lab
   ```

4. The skill checks that the target directory is not this repository's existing
   `lab/` directory.
5. The skill loads the lesson markdown files from `lab_lessons/`.
6. The skill walks the learner through one module at a time:
   - concept,
   - threat model,
   - build task,
   - exploit task,
   - defense task,
   - measurement task,
   - code explanation,
   - quiz.
7. The learner's agent writes code only in the learner-provided target
   directory.
8. At the end, the learner has a personal AI threat research lab that is
   structurally similar in learning goals but not a copy of this repository's
   implementation.

## Proposed Directory Layout

```text
lab_lessons/
├── interactive_lab_lessons_plan.md
├── README.md
├── skill/
│   └── SKILL.md
├── lessons/
│   ├── 00-orientation.md
│   ├── 01-prompt-injection.md
│   ├── 02-sensitive-information-disclosure.md
│   ├── 03-supply-chain.md
│   ├── 04-data-model-poisoning.md
│   ├── 05-improper-output-handling.md
│   ├── 06-excessive-agency.md
│   ├── 07-system-prompt-leakage.md
│   ├── 08-vector-embedding-weaknesses.md
│   ├── 09-misinformation.md
│   ├── 10-unbounded-consumption.md
│   └── 99-capstone.md
├── templates/
│   ├── lab-readme-outline.md
│   ├── attack-report-schema.json
│   └── quiz-result-schema.json
└── quizzes/
    ├── 01-prompt-injection.json
    ├── 02-sensitive-information-disclosure.json
    └── one quiz file per lesson
```

The initial implementation can start smaller than this. The final shape should
separate:

- lesson prose,
- agent skill instructions,
- reusable report/quiz schemas,
- learner-generated lab code.

## Lesson Template

Each lesson markdown file should use the same structure.

```markdown
# LLMNN: Lesson Title

## Learning Objectives

- Explain the vulnerability in plain language.
- Build a local vulnerable target.
- Run an exploit harness.
- Add a defense.
- Measure the defense delta.

## Threat Model

Describe attacker control, target behavior, safety boundary, and what counts as
success.

## Build Your Lab

Give the learner a goal and constraints, not copyable source from this repo.
Require original names, fixtures, payloads, and implementation details.

## Exploit It

Guide the learner to create payloads and an evaluator. Define expected metrics.

## Defend It

Guide the learner to add one defense and compare before/after results.

## Explain The Code

Ask the agent to explain the learner's own files, not this repository's sample
implementation.

## Quiz

Ask 3-5 short questions that check conceptual understanding and practical
tradeoffs.

## Completion Checklist

- Vulnerable target exists.
- Attack harness reports a metric.
- Defense changes the metric.
- Safety boundary is documented.
- Quiz is complete.
```

## Lesson Coverage

### 00 Orientation

Purpose:

- explain the workshop,
- create the learner's target directory,
- scaffold a minimal lab structure,
- define safety boundaries,
- explain attack success rate and defense comparisons.

Key output:

- `README.md`,
- `vulnerable-agents/`,
- `attacker/`,
- `evals/results/`,
- `writeups/`.

### 01 Prompt Injection

Learner builds a local RAG-like target with trusted and untrusted documents.

Core exploit:

- attacker-controlled retrieved content causes the agent to follow instructions
  from untrusted text.

Defense:

- untrusted-content labeling, spotlighting, or instruction/data separation.

### 02 Sensitive Information Disclosure

Learner builds a synthetic support-record target.

Core exploit:

- prompts extract fields outside the user's authorization scope.

Defense:

- retrieval scoping, data minimization, output allowlists, or secret-pattern
  blocking.

### 03 Supply Chain

Learner builds a dependency-review target using synthetic package files.

Core exploit:

- package documentation or generated files plant instructions that a coding
  agent follows.

Defense:

- dependency trust boundaries, vendored-content ignore rules, and tool
  permission gating.

### 04 Data And Model Poisoning

Learner builds a local corpus or memory fixture with a poisoned example.

Core exploit:

- a trigger phrase causes poisoned data to dominate retrieval or behavior.

Defense:

- corpus provenance, review gates, poisoning scans, and retrieval audits.

### 05 Improper Output Handling

Learner builds a downstream consumer for model output.

Core exploit:

- unsafe structured output reaches a renderer, query builder, command builder,
  or automation step.

Defense:

- schemas, encoding, allowlists, and approval gates.

### 06 Excessive Agency

Learner builds an agent with broad fake tool access.

Core exploit:

- the agent takes actions beyond the user's intended scope.

Defense:

- least-privilege tools, confirmation gates, dry-run mode, scoped credentials,
  and audit logs.

### 07 System Prompt Leakage

Learner builds a target with synthetic hidden policy text.

Core exploit:

- direct or indirect prompts reveal hidden instructions, routing rules, or
  prompt-only secrets.

Defense:

- remove secrets from prompts, separate policy from runtime secrets, and add
  prompt-leak regression tests.

### 08 Vector And Embedding Weaknesses

Learner builds a simple local retrieval index.

Core exploit:

- duplicated, adversarially similar, or poorly filtered documents skew
  retrieval.

Defense:

- metadata filters, retrieval thresholds, re-ranking, and result inspection.

### 09 Misinformation

Learner builds a grounded-answering target with stale or low-quality sources.

Core exploit:

- the agent gives confident unsupported answers.

Defense:

- citation requirements, abstention rules, freshness checks, and source
  grounding.

### 10 Unbounded Consumption

Learner builds a target that can loop, retrieve too much context, or call tools
too often.

Core exploit:

- prompts amplify token use, request count, time, or fake tool calls.

Defense:

- budgets, rate limits, recursion limits, context caps, and cancellation paths.

### 99 Capstone

Learner produces a final report:

- lab architecture,
- safety boundaries,
- per-module attack and defense results,
- lessons learned,
- future experiments.

## Skill Behavior

The lesson skill should act as a tutor and build coach.

It should:

- require a learner-provided target directory before writing files,
- refuse to use this repository's existing sample lab as the target directory,
- avoid reading sample implementation files unless the learner explicitly asks
  for high-level comparison after completing their own implementation,
- read lesson markdown files from `lab_lessons/lessons/`,
- keep a lesson progress file in the learner's target directory,
- ask the learner to confirm before moving from concept to build, exploit, and
  defense phases,
- encourage TDD-style implementation for each lab component,
- generate original code and fixtures based on the lesson requirements,
- explain the learner's generated code after each step,
- run local validation commands inside the learner's target directory,
- record quiz answers and results.

It should not:

- copy code from this repository's `lab/` directory,
- mount or inspect personal directories,
- use real credentials,
- target third-party systems,
- run destructive shell commands,
- skip safety boundary documentation.

## Anti-Copy Guardrails

The core teaching value is in building a lab, not cloning a finished one.

The skill should enforce these guardrails:

- Target directory must not be `lab/`, `tests/`, or any existing sample module
  directory from this repository.
- Generated vulnerable agents must use learner-chosen domain examples.
- Payload text must be newly generated for the learner's chosen scenario.
- Synthetic flags, secrets, package names, trigger phrases, and records must be
  different from this repository's sample markers.
- The skill should summarize concepts from this repository, but it should not
  paste implementation code from existing lab modules.
- After the learner completes a module, optional comparison can discuss design
  differences at a high level without replacing learner work.

## Quiz Model

Each lesson should end with a short quiz.

Recommended format:

- 3 multiple-choice questions,
- 1 short-answer design question,
- 1 practical debugging question.

Question types:

- identify the trust boundary,
- identify attacker control,
- interpret an attack-success metric,
- choose an appropriate defense,
- explain a false sense of security.

Quiz results should be stored in the learner's target directory, for example:

```text
evals/quiz-results/07-system-prompt-leakage.json
```

The skill should explain wrong answers briefly and point back to the relevant
lesson section.

## Safety Boundary

All lesson labs must be local, owned, and synthetic.

Lessons must not ask the learner to:

- probe third-party LLM applications,
- use real customer data,
- use real credentials,
- install real compromised packages,
- execute untrusted package scripts,
- create real cloud resources,
- send real notifications,
- perform harmful automation.

Every module should include a safety checklist in the learner's generated lab.

## Implementation Phases

### Phase 1: Lesson Plan And Skeleton

Create:

- `lab_lessons/README.md`,
- `lab_lessons/lessons/00-orientation.md`,
- one complete pilot lesson,
- `lab_lessons/skill/SKILL.md` draft,
- quiz schema.

Recommended pilot:

- LLM01 Prompt Injection, because it is the clearest entry point.

### Phase 2: Full Lesson Set

Add lessons for LLM02 through LLM10 using the shared template.

Each lesson should include:

- concept,
- threat model,
- original-build constraints,
- exploit harness requirements,
- defense requirements,
- validation commands,
- quiz.

### Phase 3: Skill Implementation

Implement the tutor skill.

Key behaviors:

- target-directory validation,
- lesson loading,
- progress tracking,
- build/exploit/defense phase gating,
- no-copy guardrails,
- quiz scoring,
- local validation guidance.

### Phase 4: Dry Run

Run the lesson system into a temporary target directory.

Validation:

- the skill does not read or copy sample lab code,
- the generated lab is original,
- each module can report a metric,
- quiz results are recorded,
- safety boundaries are present.

### Phase 5: Presentation Integration

Use the lesson system as the presentation take-away.

Presentation flow:

- show the finished research lab,
- explain one vulnerability live,
- demonstrate one lesson prompt,
- let attendees continue with the repo after the talk.

## Open Design Questions

Resolve these after the lab, blog, and presentation are complete:

- Should the skill support both Codex and Claude-specific instructions, or keep
  a single generic `SKILL.md` plus tool notes?
- Should quizzes be embedded in lesson markdown or stored as separate JSON?
- Should the learner choose a domain once for the whole lab, or choose a new
  domain per module?
- Should the final capstone generate a portfolio-style report automatically, or
  only provide an outline?

## Definition Of Done For Future Implementation

The future lesson system is complete when:

- a learner can build an original local lab in a new directory,
- all ten OWASP LLM modules have lesson files,
- each lesson includes a quiz,
- the skill enforces no-copy and safety guardrails,
- the generated lab includes measurable attack/defense comparisons,
- the presentation clearly points attendees to the lesson workflow.
