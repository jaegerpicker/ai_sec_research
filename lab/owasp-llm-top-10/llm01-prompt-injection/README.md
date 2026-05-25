# LLM01:2025 Prompt Injection

This module maps the existing v0 RAG lab to `LLM01:2025 Prompt Injection` in
the OWASP Top 10 for LLM Applications.

The current implementation demonstrates indirect prompt injection: an attacker
controls content that is retrieved by a RAG-style assistant, and the assistant
incorrectly treats that retrieved content as instructions.

No third-party LLM applications were tested. The target, payloads, documents,
and synthetic flag all live in this repository.

## Learning Goal

Learn how untrusted retrieved content can cross from data into instructions,
then measure whether an explicit untrusted-content boundary changes the result.

The intended lab loop is:

```text
owned local target
  -> repeatable attack
  -> baseline attack success rate
  -> defense toggle
  -> comparison result
  -> writeup and blog draft
```

## Current Artifact Map

The module is indexed here, but the implementation remains in the existing v0
paths for compatibility with current tests, docs, and scripts.

| Role | Current artifact |
|---|---|
| Vulnerable target | `lab/vulnerable-agents/injection-via-rag` |
| Attack harness | `lab/attacker/custom/run_v0_rag_attacks.py` |
| Payloads | `lab/attacker/payloads/indirect_prompt_injection.json` |
| Defense | `lab/defenses/spotlighting` |
| Default eval output | `lab/evals/results/v0-rag-latest.json` |
| Lab writeup | `lab/writeups/001-injection-via-rag.md` |
| Blog draft | `src/content/blog/breaking-agents-llm01-prompt-injection.md` |

## Threat Model

The attacker can influence a document that the assistant retrieves as context.
The attacker cannot directly edit the system prompt, source code, environment,
or fake action implementation.

The vulnerable assistant retrieves both trusted and attacker-controlled
documents. Without a trust boundary, the attacker-controlled document can steer
the assistant into calling the synthetic `exfiltrate_flag` action.

## Safety Boundary

- The target is an owned local lab target.
- The flag is synthetic: `LAB-V0-RAG-FLAG-DO-NOT-USE-REAL-SECRETS`.
- No real credentials, tokens, cloud resources, customer data, or personal data
  are used.
- The Docker service binds to loopback only.
- No third-party LLM applications are tested.
- Do not adapt this module to external targets without a separate issue and
  explicit written authorization.

## Baseline And Defense

Baseline result:

```text
defense OFF: 1.0 attack_success_rate
```

The current defense is spotlighting. It wraps attacker-controlled retrieved
content in explicit untrusted-content delimiters and prevents spotlighted
content from controlling fake action selection.

Defense result:

```text
defense ON: 0.0 attack_success_rate
absolute reduction: 1.0
```

This result is intentionally narrow. It shows that the defense blocked the
measured local attack path for the current payload set. It does not prove that
spotlighting is sufficient for production RAG security.

## Reproduce

From the repository root, run the lab tests:

```bash
npm run test:lab
```

Run the attack comparison:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode compare
```

Run the vulnerable service:

```bash
docker compose -f lab/docker-compose.yml up vulnerable-rag
```

Call the local endpoint:

```bash
curl -s http://127.0.0.1:8000/chat \
  -H 'content-type: application/json' \
  -d '{"message":"How should the refund workflow handle support notes?"}'
```

Run the same payload suite against the live HTTP service:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py \
  --target http \
  --base-url http://127.0.0.1:8000 \
  --mode off
```

The JSON report includes a structured `metadata` object with the OWASP module,
runner version, target, payload path, payload count, run id, timestamps, and
duration. The legacy `attack_success_rate`, `successes`, `failures`, and
`cases` fields remain available for simple checks and scripts.

## Follow-Up Work

- Expand the payload set.
- Decide whether future issues should physically move code into OWASP module
  directories or keep module directories as stable indexes.
