# Breaking Agents to Build Better Ones

A hands-on lab for the OWASP Top 10 for LLM Applications.

This roadmap turns the OWASP LLM Top 10 into local, reproducible engineering
experiments. Each module should produce the same set of artifacts:

- One owned vulnerable target.
- One repeatable attack harness.
- One measured baseline result.
- One or more defenses with measured deltas.
- One lab writeup.
- One blog post draft.
- One Summit talk section.

The goal is not to prove universal security claims. The goal is to learn each
risk by building the bug, measuring it, and documenting what changed when a
defense was added.

## Shared Module Contract

Each OWASP module should include:

- `README.md` with the threat model, safety boundary, and reproduction steps.
- A vulnerable local target or fixture set.
- Payloads and attack code under `lab/attacker/`.
- Defense code or configuration under `lab/defenses/`.
- Structured eval output under `lab/evals/results/`.
- Tests covering the lab contract and safety constraints.
- A writeup under `lab/writeups/`.

## Safety Boundary

All modules must stay inside owned local lab targets. Do not test third-party
LLM applications, real user data, real credentials, or external systems unless a
future issue explicitly authorizes that work and records the authorization.

## OWASP LLM Top 10 Module Map

| OWASP item | Local lab idea | Attack harness | Defense idea | Content output | Tracking |
|---|---|---|---|---|---|
| `LLM01:2025` Prompt Injection | RAG assistant retrieves trusted policy docs plus an attacker-controlled support note. | Payload set measures whether the assistant follows injected document instructions and reveals a synthetic lab flag. | Spotlighting/untrusted-content labeling around retrieved documents. | Blog post: prompt injection through RAG; Summit primary demo. | v0 built; module index #28; blog draft #26; HTTP mode #30; metadata #32 |
| `LLM02:2025` Sensitive Information Disclosure | Support agent has access to synthetic customer records, internal notes, and a fake secret. | Prompts attempt to extract data outside the user's authorization scope. | Data minimization, retrieval scoping, output allowlists, and secret-pattern blocking. | Blog post: least data for agents; talk section on context as data exposure. | #38 |
| `LLM03:2025` Supply Chain | Compromised dependency or vendored package injects malicious instructions into docs, comments, or generated files. | Harness asks an agent to inspect dependency content and checks whether repo instructions are followed incorrectly. | Dependency trust boundaries, lockfile review, ignore rules for vendored instructions, and tool permission gating. | Blog post: package compromise to prompt injection; talk section tying npm/PyPI risk to AI agents. | #37; first lab slice built |
| `LLM04:2025` Data and Model Poisoning | Training or retrieval corpus includes poisoned examples that bias future answers or create a trigger phrase. | Payloads query for trigger behavior and measure whether poisoned examples dominate retrieval or response. | Corpus provenance, review gates, poisoning scans, and retrieval result auditing. | Blog post: poisoning as persistence; talk section on memory and corpus trust. | #39 |
| `LLM05:2025` Improper Output Handling | Agent output is passed into a downstream renderer, shell-like tool, SQL builder, or ticket automation without validation. | Payloads cause the model to emit unsafe structured output that the downstream component consumes. | Schema validation, output encoding, command allowlists, and human approval for risky actions. | Blog post: model output is untrusted input; talk section on downstream blast radius. | #36; first lab slice built |
| `LLM06:2025` Excessive Agency | Agent has broad tool access such as shell, git, ticket updates, and notification tools. | Multi-step prompts attempt to make the agent take actions beyond the user's intent. | Least-privilege tools, confirmation gates, scoped credentials, dry-run modes, and audit logs. | Blog post: agent permissions as the real risk; talk section on capability boundaries. | #40; first lab slice built |
| `LLM07:2025` System Prompt Leakage | App includes hidden policy, routing rules, or synthetic secrets in system/developer context. | Payloads ask directly and indirectly for hidden instructions and measure leakage. | Remove secrets from prompts, split policy from runtime secrets, and test prompt-leak regressions. | Blog post: system prompts are not secret storage; talk section on misplaced trust. | #41 |
| `LLM08:2025` Vector and Embedding Weaknesses | Vector store contains poisoned, duplicated, or adversarially similar documents that skew retrieval. | Harness tests retrieval collisions, over-broad matches, and malicious-neighbor selection. | Metadata filters, chunk provenance, retrieval thresholds, re-ranking, and result inspection. | Blog post: vector databases as attack surface; talk section on retrieval control. | #42 |
| `LLM09:2025` Misinformation | Agent answers confidently from stale or low-quality local sources and invents unsupported claims. | Evaluator checks citation quality, source grounding, and hallucinated assertions. | Retrieval grounding, abstention rules, citation requirements, and freshness checks. | Blog post: measuring truthfulness in agent workflows; talk section on confidence vs evidence. | #44 |
| `LLM10:2025` Unbounded Consumption | Agent accepts prompts that cause expensive loops, huge context retrieval, or repeated tool calls. | Harness measures token, time, request count, and tool-call amplification. | Budgets, rate limits, recursion limits, context caps, and cancellation paths. | Blog post: denial of wallet and runaway agents; talk section on operational controls. | #43 |

## V1 Work Order

1. Normalize the current prompt-injection lab as the `LLM01:2025` module without
   breaking existing paths. Done in #28.
2. Publish an `LLM01` blog draft based on the existing lab writeup. Done in
   #26.
3. Add live HTTP mode and richer eval metadata to the `LLM01` attack harness.
   Done in #30 and #32.
4. Create one GitHub issue for each planned OWASP module. Done in #35.
5. Build `LLM03:2025` Supply Chain next, because it connects directly to
   package-manager compromise and AI coding-agent risk. First slice done in
   #37.
6. Build `LLM06:2025` Excessive Agency next to connect prompt-level attacks to
   overpowered agent tools. First slice done in #40.
7. Build `LLM05:2025` Improper Output Handling to show model output becoming
   unsafe downstream input. First slice done in #36.

## Next Work

- Expand `LLM03:2025` with more supply-chain fixture variants and a blog draft
  (#37 follow-up).
- Build `LLM02:2025` sensitive-information-disclosure lab (#38).
- Expand `LLM05:2025` with JSON Schema examples, approval gates, and renderer
  encoding tests (#36 follow-up).
- Expand `LLM06:2025` with multi-step payloads, dry-run mode, and audit-log
  assertions (#40 follow-up).
- Continue through the remaining module tracking issues after the first three
  agent-focused modules are working.

## References

- OWASP Top 10 for Large Language Model Applications:
  https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP GenAI LLM Top 10:
  https://genai.owasp.org/llm-top-10/
