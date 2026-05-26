# LLM06: Excessive Agency

This writeup documents the first LLM06 excessive-agency lab slice: a synthetic
agent has broad fake tool access, and attacker prompts try to push it beyond the
intended support workflow.

No real shell commands run, no real credentials are used, and no external side
effects occur.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/excessive-agency-agent/
```

It exposes three risky fake actions:

- `run_shell_command`
- `push_git_change`
- `send_notification`

Each action returns a synthetic marker instead of touching the host, git remotes,
or messaging systems.

## Attack

The attack models a user who asks for a normal support task and then pressures
the agent into taking extra actions: deleting logs, pushing a branch, or sending
a team notification.

In the vulnerable baseline, the agent treats broad tool access as permission to
act. That is the excessive-agency lesson: the dangerous boundary is often not
what the model says, but what the model is allowed to do.

## Defense

The defense is a least-privilege confirmation gate. Risky tools are still known
to the agent, but requests to use them are blocked until a human approves the
specific action.

This is not a full production policy engine. It is a small experiment showing
that broad tools need scope checks, confirmation gates, dry-run defaults, and
auditability.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm06_excessive_agency_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add multi-step payloads where the risky action is hidden behind benign setup.
- Add dry-run mode and audit-log assertions.
- Compare confirmation gating with tool-scoped credentials.

## Blog And Talk Notes

For the blog series, the key framing is that capability boundaries matter more
than prompt wording. A weak instruction-following decision becomes materially
riskier when the agent has broad tools.

For the Summit talk, this module is the natural bridge from prompt injection to
agent permissions: the same class of model mistake has a larger blast radius
when tools are overpowered.
