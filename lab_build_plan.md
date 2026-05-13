# AI Security Research Lab — Build Plan

A personal, reproducible lab for hands-on AI red-team research. The lab itself is a portfolio piece ("I built and operate an AI red-team lab"). Everything runs locally on the MBP plus a cheap VPS for any internet-facing pieces.

## Design Principles

1. **Isolation first.** Vulnerable agents never touch real credentials, real cloud, or my personal data. Separate Docker network, dedicated cloud sub-account, no shared volumes.
2. **Reproducibility.** Everything is `docker compose up`. A fresh clone of the repo + an API key gets the whole lab running.
3. **Attack + defense + measurement.** Every vulnerability gets a corresponding eval. If I can't measure attack-success-rate, I haven't really studied it.
4. **Public by default.** Code lives in a public GitHub repo (`ai-redteam-lab`). README double-serves as portfolio.
5. **Safety.** No real CSAM/bio/cyber-uplift testing. Stick to OWASP-canonical attack classes. Read Anthropic's responsible disclosure policy before anything that hits a hosted model.

## v0 First Milestone

The full roadmap below remains the long-term research plan. v0 is the first
small, complete slice: one vulnerable agent, one attack path, one eval, one
defense toggle, and one writeup. This keeps the first release achievable while
preserving the broader plan for tool attacks, memory poisoning, scheduled
hijack, cross-agent injection, and defense comparisons.

### v0 Scope

- **Target:** one intentionally vulnerable RAG agent focused on indirect prompt
  injection through retrieved documents.
- **Attack surface:** trusted and attacker-controlled document fixtures,
  plus a deterministic fake tool/action surface before adding real MCP.
- **Attack harness:** a small scripted payload set that reports attack success
  rate over repeated attempts.
- **Defense:** one toggle, preferably untrusted-content labeling or
  spotlighting, measured as defense OFF vs defense ON.
- **Writeup:** a reproducible report covering architecture, safety boundaries,
  attack steps, eval results, and defense delta.

### v0 Deliverable

`docker compose up` runs the local vulnerable RAG agent; one command runs the
attack/eval harness; the output reports attack success rate; one defense toggle
produces a comparable result; and the writeup explains how to reproduce the
experiment safely.

### Later Roadmap

After v0, continue through the original phases rather than replacing them:

- Add tool-confusion and excessive-agency agents.
- Add memory-poisoning, scheduled-hijack, and cross-agent-leak agents.
- Introduce garak, PyRIT, promptfoo, and Inspect where each adds useful
  coverage.
- Expand defenses and compare attack success rate across the matrix.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Host (MBP)                                                 │
│                                                             │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │ Vulnerable   │   │ Attacker     │   │ Eval Harness │    │
│  │ Agent(s)     │←─→│ Harness      │←─→│ (Inspect /   │    │
│  │ (DVLA-like)  │   │ (garak,      │   │  promptfoo)  │    │
│  │              │   │  PyRIT,      │   │              │    │
│  │ FastAPI +    │   │  custom)     │   │              │    │
│  │ MCP tools    │   │              │   │              │    │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘    │
│         │                  │                  │             │
│         └──────────────────┴──────────────────┘             │
│                    │ Docker network: redteam-lab            │
│                    │ (no host network, no internet)         │
│                    │                                        │
│  ┌──────────────────────────────────────────────────┐      │
│  │ Egress proxy (mitmproxy) — logs every LLM call   │      │
│  └──────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
                         │
                  Anthropic / OpenAI APIs
                  (via dedicated, low-limit key)
```

## Components

### 1. Vulnerable Agent Suite (`vulnerable-agents/`)
Multiple intentionally vulnerable agents, each isolating one attack class:

| Agent | Vulnerability | Source of inspiration |
|---|---|---|
| `injection-via-rag` | Indirect prompt injection through retrieved documents | Embrace The Red |
| `tool-confusion` | Two MCP tools with overlapping verbs; attacker steers tool selection | Own research |
| `memory-poisoning` | Persistent "skills/feedback" memory writable from user input | Mirrors Claude Code memory model |
| `scheduled-hijack` | Agent with cron-style scheduler tool | Mirrors `/schedule` |
| `cross-agent-leak` | Two agents that exchange notes via a shared doc | Multi-agent attack class |
| `excessive-agency` | Agent given shell + git + Slack tools with no confirmation gating | OWASP LLM06 |

Each agent: small FastAPI service, exposes `/chat`, ships its own MCP tool server, has a `flag.txt` the attacker is trying to exfiltrate.

### 2. Attacker Harness (`attacker/`)
- **garak** — NVIDIA's LLM vuln scanner, baseline coverage.
- **PyRIT** — Microsoft's red-team orchestrator, multi-turn attacks.
- **promptfoo red-team mode** — payload library.
- **Custom Python framework** — for novel attacks specific to my agents (the interesting research output).

### 3. Eval Harness (`evals/`)
- **Inspect (UK AISI)** as primary framework — research-credible, what AISI uses.
- Each attack has a paired eval: "given attack class X, what % of N trials succeed against agent Y?"
- Results stored in SQLite, plotted with a small Streamlit dashboard.

### 4. Egress proxy (`proxy/`)
- mitmproxy logs every outbound LLM call.
- Used to (a) audit token spend, (b) inspect what the agents send when attacked, (c) catch agents trying to exfil to attacker-controlled URLs.

### 5. Defense modules (`defenses/`)
Plug-in defenses I can A/B test:
- Input sanitization (Lakera-style content classifier).
- Tool-call confirmation gating.
- Spotlighting (Microsoft's research).
- Output validation against allowlist.
- Conversation-level anomaly detection.

Each defense has an eval delta: "attack success rate, defense ON vs OFF."

## Repo Structure

```
ai-redteam-lab/
├── README.md                 # Portfolio-grade write-up
├── docker-compose.yml        # One-command bring-up
├── vulnerable-agents/
│   ├── injection-via-rag/
│   ├── tool-confusion/
│   ├── memory-poisoning/
│   ├── scheduled-hijack/
│   ├── cross-agent-leak/
│   └── excessive-agency/
├── attacker/
│   ├── garak-configs/
│   ├── pyrit-flows/
│   └── custom/
├── evals/
│   ├── inspect-tasks/
│   ├── dashboard/
│   └── results.sqlite
├── proxy/
│   └── mitmproxy-config/
├── defenses/
│   ├── input-filter/
│   ├── tool-gating/
│   ├── spotlighting/
│   └── output-validation/
├── writeups/
│   ├── 001-injection-via-rag.md
│   ├── 002-tool-confusion.md
│   └── ...
└── .github/workflows/
    └── nightly-evals.yml     # CI runs evals nightly, posts deltas
```

## Build Phases

### Phase 1 — Foundation (Week 1)
- [ ] Repo skeleton, MIT license, README v0.
- [ ] Docker compose with one vulnerable agent (`injection-via-rag`) + mitmproxy.
- [ ] Dedicated Anthropic API key with low spend cap.
- [ ] Inspect installed, one trivial eval running.

**Deliverable:** `docker compose up` runs a vulnerable RAG agent; one manual attack works; one Inspect task scores it.

### Phase 2 — First Attack Class (Week 2)
- [ ] Build out `injection-via-rag` to ~10 indirect-injection payload variants.
- [ ] Wire garak against it.
- [ ] First Inspect eval suite with attack-success-rate plot.
- [ ] Writeup `001-injection-via-rag.md` → becomes blog post material.

### Phase 3 — Tool Attacks (Weeks 3–4)
- [ ] `tool-confusion` agent + 2 MCP servers.
- [ ] `excessive-agency` agent with shell tool (sandboxed via gVisor or Firecracker).
- [ ] PyRIT multi-turn flow against both.
- [ ] Writeups 002, 003.

### Phase 4 — Persistence + Multi-Agent (Weeks 5–6)
- [ ] `memory-poisoning`, `scheduled-hijack`, `cross-agent-leak`.
- [ ] Custom attacker framework for these (off the beaten path; less tooling exists).
- [ ] Writeups 004, 005, 006.

### Phase 5 — Defenses (Weeks 7–8)
- [ ] Implement 4 defense modules.
- [ ] A/B eval each against each attack class. Matrix of results.
- [ ] **Capstone blog post:** "What actually works against agent attacks: an evidence-based comparison."

### Phase 6 — Public Launch (Week 9+)
- [ ] Polish README to portfolio quality (architecture diagram, badges, demo gif).
- [ ] Submit a talk to AI Village / BSides / local OWASP chapter using lab as the demo.
- [ ] Submit one finding (if any meets bar) to Anthropic / OpenAI bug bounty.
- [ ] Open issues inviting community attack contributions.

## Hardware & Cost

- **MBP** handles everything for local agents + small models.
- **API spend** target: $20/month cap on dedicated key. Most evals run against `claude-haiku-4-5`; Sonnet/Opus only for spot-checks.
- **Optional VPS** ($5–10/mo Hetzner) only if I want a 24/7 internet-facing target for indirect-injection-via-web experiments.
- **Optional GPU** (Lambda Labs / Runpod, ~$0.50/hr) only when running open-weight models (Llama, Qwen) for membership-inference or training-data-extraction work. Not needed for the first 8 weeks.

## Safety / Ethical Guardrails

- All targets are mine. No probing of third-party LLM apps without explicit written authorization.
- Stick to OWASP-canonical attack classes (prompt injection, tool abuse, excessive agency). No CBRN, no real CSAM, no detection-evasion-for-malicious-purposes.
- Anything that touches a hosted model: pre-check the provider's responsible disclosure / acceptable use policy.
- Bug bounty submissions go through proper channels; no public 0-day drops.
- Lab is isolated: no shared host volumes, no real creds anywhere in the agent containers, no host network mode.

## Success Criteria

By end of Phase 6:
- Public repo with ≥6 vulnerable agents, ≥6 writeups, working eval dashboard.
- ≥2 blog posts published.
- ≥1 conference talk submitted (accepted or not — submission itself is a portfolio piece).
- ≥1 bug bounty submission to a major AI provider.
- ≥1 OSS contribution upstreamed to garak / Inspect / promptfoo.

If I hit that, the resume narrative writes itself.
