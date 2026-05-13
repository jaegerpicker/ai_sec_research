# AI Red-Team Lab v0

This directory contains the local AI red-team lab implementation. The v0 goal
is a small, reproducible slice of the larger roadmap: one vulnerable RAG agent,
one indirect prompt injection attack path, one evaluation harness, one defense
toggle, and one writeup.

The first implementation target is `vulnerable-agents/injection-via-rag`.
Issue #7 adds the vulnerable FastAPI target. The attack runner, defense toggle,
and writeup are tracked in follow-up issues.

## Layout

```text
lab/
├── docker-compose.yml
├── vulnerable-agents/
│   └── injection-via-rag/
├── attacker/
│   ├── custom/
│   └── payloads/
├── evals/
│   └── results/
├── defenses/
│   └── spotlighting/
├── proxy/
│   └── logs/
└── writeups/
```

## Safety Boundaries

- No real credentials.
- No real cloud tokens.
- No personal data mounted into vulnerable services.
- No host network mode.
- Local services bind to loopback only when host access is needed.
- No third-party targets without explicit written authorization.

The lab is intentionally vulnerable. Keep vulnerable behavior inside owned,
local lab services.

## Local Commands

From this directory:

```bash
docker compose config
docker compose up
```

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r lab/requirements.txt
npm run test:lab
.venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py
```

The initial `vulnerable-rag` service publishes only `127.0.0.1:8000` for local
testing. Later issues replace the placeholder proxy behavior with attack
harness and evaluation flow.

The v0 attack runner writes machine-readable JSON results to
`lab/evals/results/v0-rag-latest.json` by default. Generated result files are
ignored by Git so repeated local evals do not create repository noise.
