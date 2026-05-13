# AI Red-Team Lab v0

This directory contains the local AI red-team lab implementation. The v0 goal
is a small, reproducible slice of the larger roadmap: one vulnerable RAG agent,
one indirect prompt injection attack path, one evaluation harness, one defense
toggle, and one writeup.

The first implementation target is `vulnerable-agents/injection-via-rag`.
Issue #6 only creates the scaffold. The vulnerable agent, attack runner,
defense toggle, and writeup are tracked in follow-up issues.

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
npm run test:lab
```

The initial Docker Compose file is a service skeleton. Later issues replace the
placeholder commands with the vulnerable RAG agent, proxy behavior, attack
harness, and evaluation flow.
