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
- data and model poisoning,
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

## 23. Q&A

Questions, objections, and lab ideas.

Good prompts:

- Which agent input path worries you most?
- Which tool permission would you remove first?
- What would make this lab useful in your review process?

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
# Measured comparison, from repo root
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode compare
cat lab/evals/results/v0-rag-latest.json

# Optional visual HTTP target in Terminal 1
cd lab
docker compose up --build

# Optional HTTP smoke in Terminal 2, from repo root
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --target http --mode off
```

The demo runbook will expand this into a timed live path and fallback path.

---

## Appendix C. Full Module Map

| Item | Local module |
|---|---|
| LLM01 Prompt Injection | [`llm01-prompt-injection`](../../lab/owasp-llm-top-10/llm01-prompt-injection/README.md) |
| LLM02 Sensitive Information Disclosure | [`llm02-sensitive-information-disclosure`](../../lab/owasp-llm-top-10/llm02-sensitive-information-disclosure/README.md) |
| LLM03 Supply Chain | [`llm03-supply-chain`](../../lab/owasp-llm-top-10/llm03-supply-chain/README.md) |
| LLM04 Data and Model Poisoning | [`llm04-data-model-poisoning`](../../lab/owasp-llm-top-10/llm04-data-model-poisoning/README.md) |
| LLM05 Improper Output Handling | [`llm05-improper-output-handling`](../../lab/owasp-llm-top-10/llm05-improper-output-handling/README.md) |
| LLM06 Excessive Agency | [`llm06-excessive-agency`](../../lab/owasp-llm-top-10/llm06-excessive-agency/README.md) |
| LLM07 System Prompt Leakage | [`llm07-system-prompt-leakage`](../../lab/owasp-llm-top-10/llm07-system-prompt-leakage/README.md) |
| LLM08 Vector and Embedding Weaknesses | [`llm08-vector-embedding-weaknesses`](../../lab/owasp-llm-top-10/llm08-vector-embedding-weaknesses/README.md) |
| LLM09 Misinformation | [`llm09-misinformation`](../../lab/owasp-llm-top-10/llm09-misinformation/README.md) |
| LLM10 Unbounded Consumption | [`llm10-unbounded-consumption`](../../lab/owasp-llm-top-10/llm10-unbounded-consumption/README.md) |

---

## Appendix D. Metric Notes

- Attack success rate is `successful attacks / total attempts`.
- Compare defense-off and defense-on runs with the same payload set.
- Treat the delta as a lab signal, not a universal security claim.
- Keep result JSON with runner metadata, target type, payload path, and cases.

---

## Appendix E. References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [Repo lab roadmap](../../lab/owasp-llm-top-10/roadmap.md)
- [LLM01 writeup](../../lab/writeups/001-injection-via-rag.md)
