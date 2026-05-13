---
title: "Supply Chain Attacks on AI Tooling: Lessons from Shai-Hulud"
description: "A field report on the npm worm that targeted ~/.claude/, the three scanners I built in response, and what AI infra security needs next."
pubDate: 2026-05-13
draft: true
tags: ["supply-chain", "npm", "shai-hulud", "ai-tooling", "claude-code"]
---

> **Draft.** Outline below; prose to follow. Internal hostnames, ticket IDs,
> and employee names need to be sanitized before publication.

## Hook

When Mini Shai-Hulud hit npm in late 2025, the payload of interest wasn't a
stealer or miner — it was `~/.claude/router_runtime.js`. The attackers were
*specifically* targeting AI developer environments. Why? Because the AI dev
workstation is the new high-value endpoint: it has shell, cloud creds, source
access, *and* an LLM that will helpfully run whatever it reads.

## Why AI dev environments are now a prime target

- Concentration of secrets: cloud, GitHub, Jira, Slack, prod DB tokens.
- LLM-as-execution-substrate: the worm doesn't need to escape; it just needs
  to land somewhere the LLM will read.
- Skills, hooks, and MCP servers are *executable configuration* — they look
  like data but run like code.
- Persistence is novel: LaunchAgent, systemd user units, *and* `CLAUDE.md`
  memory entries that re-execute every session.

## Anatomy of Mini Shai-Hulud

- Initial vector: compromised npm package via maintainer phishing.
- Postinstall hook drops `router_runtime.js` into `~/.claude/`.
- Persistence: LaunchAgent on macOS, systemd user unit on Linux.
- Dead-drop: git commits to attacker-controlled branches; ransom-marker npm
  tokens.
- Why traditional EDR missed it: artifacts live inside a developer's home
  directory and look like normal AI tooling config.

## What I built in response

- **host-compromise-scan** — POSIX-sh scanner that runs offline (no C2 tipoff)
  and looks for known-bad SHA-256s, injected `@tanstack/setup` packages,
  dead-drop git refs, ransom-marker tokens, and persistence artifacts. Two
  variants: dev-laptop (macOS+Linux) and minimal container (Alpine, Distroless).
- **compromised-package-audit** — pulls the live StepSecurity tracking list,
  searches the entire codebase (npm + PyPI manifests) via internal code search.
- **artifactory-compromise-history** — checks the Artifactory cache to
  identify *which* developer or CI account downloaded a compromised version,
  when, and how many times. Turns a fleet-wide "are we exposed?" into a
  named-person triage list within minutes.

## Generalizable lessons for AI infra security

- Treat the AI dev environment as a Tier-0 asset. `CLAUDE.md`,
  `.claude/skills/`, and `.claude/hooks/` are code, not config.
- Pin and verify everything postinstall. npm/PyPI postinstall hooks are the
  new macro-virus.
- Cache layer = forensics gold. Artifactory/JFrog/Nexus logs name the actual
  user who pulled the bad artifact. Most orgs don't realize this is queryable.
- Build offline scanners. C2 tipoff is real; any scanner that beacons home
  is broken.
- Skills/MCP servers need supply-chain provenance — pinning, signing,
  allowlist. Right now it's the wild west.

## What's next

- A signed-skill spec proposal (cosign / sigstore for `.claude/skills/`).
- Threat model for MCP server install flows.
- Detection rules for the next AI-tooling-targeted worm.
