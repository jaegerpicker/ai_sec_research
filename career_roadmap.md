# AI Security / AI Red Teaming — Career Roadmap

> Personal study + transition plan for moving from security/software engineering into AI security research, AI red teaming, and AI pentesting.

Given my background (security engineering + daily Claude Code use + production agent systems), I'm already ~60% of the way there. The field splits into four overlapping tracks. Pick one as primary; let the others fill in.

## Framing

- **"AI Security" is four jobs sharing a buzzword.** Hiring managers conflate them — my resume needs to pick a lane.
- **My agent-building experience is a rare credential.** Most "AI security researchers" have never shipped an agent in production. "I've built and broken agentic systems" beats most certs.

---

## The Four Tracks

**1. AI Red Team / Offensive AI Security**
Prompt injection, jailbreaks, agent hijacking, tool abuse, indirect injection via RAG/email/web. My Claude Code agent experience pays off most directly here.
*Roles:* Anthropic Frontier Red Team, OpenAI Red Team, Microsoft AI Red Team, HiddenLayer, Lakera, Robust Intelligence (Cisco), HackerOne AI programs.

**2. ML / Model Security**
Adversarial ML, model extraction, membership inference, training-data extraction, watermarking, fine-tuning attacks. Heavier math/ML background.
*Roles:* Trail of Bits, NCC Group ML practices, academic-adjacent research labs.

**3. AI Application / Infra Security (AppSec for AI)**
Securing LLM-powered apps: prompt firewalls, MCP server hardening, tool-call sandboxing, OAuth-for-agents, output validation, supply chain (compromised models/datasets, à la Shai-Hulud). Closest to traditional AppSec. Highest hiring volume right now.

**4. Governance / AI Risk / Evaluations**
Model evals, red-team-as-process, RAI frameworks, EU AI Act compliance. Lower technical depth, more policy-flavored.

**My primary target:** Track 1 (AI Red Team) with Track 3 (AI AppSec) as fallback — both leverage existing experience.

---

## Foundational Study (regardless of track)

**Read end to end:**
- OWASP Top 10 for LLM Applications (2025)
- OWASP Agentic AI Threats and Mitigations
- MITRE ATLAS — adversarial threat landscape for AI
- NIST AI Risk Management Framework + Generative AI Profile
- Anthropic's "Constitutional AI" and "Sleeper Agents" papers
- Simon Willison's blog (simonwillison.net) — entire prompt-injection tag
- Embrace The Red (embracethered.com, Johann Rehberger) — practical agent exploitation writeups

**Hands-on labs:**
- Gandalf (Lakera) — entry-level prompt injection CTF
- HackTheBox AI Red Team track
- PortSwigger Web Security Academy LLM module
- DEF CON AI Village CTF archives
- AI Goat, Damn Vulnerable LLM Agent

## Technical Depth

- **Transformers from scratch** — Karpathy's "Let's build GPT" + nanoGPT
- **Fine-tuning + RLHF basics** — HuggingFace course; SFT vs DPO vs RLHF
- **Adversarial ML** — Nicholas Carlini's papers (start with "Are aligned neural networks adversarially aligned?")
- **Agent architectures** — ReAct, tool use, MCP spec (already known)
- **Evals** — Inspect (UK AISI), promptfoo, Anthropic evals cookbook, garak

## Certifications (honest take)

| Cert | Worth it? |
|---|---|
| HackTheBox CAIRT | **Yes** — most hands-on, technically respected |
| SANS SEC545 / AIS247 | Yes if employer pays |
| CompTIA SecAI+ / vendor AI certs | Skip — marketing |
| ISC2 / ISACA AI certs | Only for governance track |
| Keep existing: OSCP, OSWE, GWAPT | **More valuable** than AI-branded certs |

**Better than any cert:** public portfolio. One HackerOne LLM bug, one Embrace-The-Red-style writeup, one OSS contrib to garak/promptfoo/Inspect.

---

## 90-Day Plan

| Weeks | Focus |
|---|---|
| 1–2 | OWASP LLM Top 10, ATLAS, NIST GenAI. Beat Gandalf. |
| 3–4 | Karpathy GPT video; build nanoGPT. |
| 5–6 | Build vulnerable agent; attack it; document. → Blog post #1 |
| 7–8 | Submit to AI bug bounty (Anthropic, OpenAI, Google, HackerOne). |
| 9–10 | Contribute to garak or promptfoo. |
| 11–12 | Submit talk to BSides / DEF CON AI Village / OWASP chapter. |

## Communities

- DEF CON AI Village Discord
- OWASP GenAI Security Project working groups
- MLSecOps (Protect AI)
- AI Village Slack

**Follow:** @simonw, @karpathy, @nicholascarlini, @wunderwuzzi23 (Johann Rehberger), @riley_goodside, @random_walker.

---

## Leveraging My Brivo Context

Work I've already done that counts as AI security experience:
- **host-compromise-scan + compromised-package-audit + artifactory-compromise-history** — supply-chain incident response for AI tooling (Shai-Hulud). Publishable (sanitized).
- **Agentic systems via MCP** — direct experience with agent attack surface.
- **brivo-agents (Investigator/Botvo)** — autonomous-agent guardrails in production.

**Transition narrative:**
> "I've built and operated autonomous agents in production at scale, including supply-chain incident response for AI tooling. I want to do that adversarially."

Stronger than "I want to pivot into AI security."
