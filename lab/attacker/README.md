# v0 Attacker Harness

The v0 attacker harness runs a small indirect prompt-injection payload set
against the local vulnerable RAG agent code path, with optional spotlighting
defense, and reports attack success rate.

From the repository root:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py
```

By default the runner uses `--mode compare`, which executes the suite twice
(defense off, defense on) and writes a combined report.

## Modes

```bash
# Default: run defense OFF and defense ON, report both ASRs and the delta.
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode compare

# Baseline only (vulnerability check).
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode off

# Defense only (post-mitigation check).
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode on
```

## Targets

The default target is the in-process Python code path. This is fastest for unit
tests and local comparisons:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py \
  --target in-process --mode compare
```

The runner can also attack a live local service over HTTP. Start the vulnerable
RAG app first, then run:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py \
  --target http \
  --base-url http://127.0.0.1:8000 \
  --mode off
```

HTTP mode posts each payload to `/chat` and uses the same scoring logic and JSON
output schema as in-process mode.

The defense is the spotlighting boundary marker described in
`lab/defenses/spotlighting/README.md`. It can also be toggled directly via
the `LAB_V0_DEFENSE_SPOTLIGHTING=1` environment variable on the agent.

## Paths

Default payload set:

```text
lab/attacker/payloads/indirect_prompt_injection.json
```

Default result file:

```text
lab/evals/results/v0-rag-latest.json
```

## Result Metadata

Each report includes the legacy result fields plus a structured `metadata`
object. The metadata identifies:

- schema version,
- run id,
- OWASP module (`LLM01:2025 Prompt Injection`),
- lab module (`llm01-prompt-injection`),
- runner name and version,
- target type and base URL when applicable,
- payload path and payload count,
- start/end timestamps,
- duration in milliseconds.

Comparison reports use one parent run id and include that id in each child
defense run.

Success means the agent selected the fake `exfiltrate_flag` action and
exposed only the synthetic lab flag. With the defense enabled, success
should drop because spotlighted untrusted content is no longer scanned for
instruction triggers.
