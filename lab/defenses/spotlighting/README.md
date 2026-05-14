# Spotlighting Defense

Spotlighting is a boundary-marker defense for indirect prompt injection,
described in Microsoft Research's *Defending Against Indirect Prompt
Injection Attacks With Spotlighting* (2024). The technique labels content
that came from untrusted sources so an agent treats it as data, not
instructions.

## v0 implementation

`spotlighting.py` exposes one function, `apply_spotlighting(documents)`:

- For every retrieved document whose `trust` is `"trusted"`, it tags the doc
  with `spotlighted = False` and leaves the content unchanged.
- For every other document, it wraps the content in
  `<<UNTRUSTED>>...<</UNTRUSTED>>` delimiters and tags it with
  `spotlighted = True`.

The v0 vulnerable RAG agent calls `apply_spotlighting` when the defense is
enabled and then restricts its action selector to non-spotlighted content.
Instruction-like triggers (`exfiltrate_flag`) inside spotlighted content no
longer cause the agent to act.

## Toggle

Set the environment variable `LAB_V0_DEFENSE_SPOTLIGHTING=1` to enable the
defense at runtime. Anything else (unset, `0`, `false`) keeps the defense
off. No code edit is required.

```bash
LAB_V0_DEFENSE_SPOTLIGHTING=1 .venv/bin/uvicorn app:app \
  --app-dir lab/vulnerable-agents/injection-via-rag \
  --host 127.0.0.1 --port 8000
```

The attack runner exposes the same toggle through `--mode`:

```bash
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode compare
```

`compare` runs the suite twice (defense off, defense on) and reports both
attack success rates in one JSON file.

## Limitations

This v0 defense is intentionally simple. Production spotlighting also
datamarks token boundaries or base64-encodes untrusted content so that a
model ignoring the delimiters still cannot read instructions verbatim. For
the v0 toy agent, delimiters plus action-selector scope restriction are
enough to show a measurable OFF vs ON delta.
