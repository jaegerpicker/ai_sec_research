# LLM02: Sensitive Information Disclosure

This writeup documents the first LLM02 sensitive-information-disclosure lab
slice: a synthetic support agent retrieves records that include scoped support
summaries, internal notes, and synthetic secrets.

No real credentials, personal data, production data, or third-party targets are
used.

## Architecture

The target lives at:

```text
lab/vulnerable-agents/sensitive-records-agent/
```

It contains a small JSON record set:

```text
lab/vulnerable-agents/sensitive-records-agent/records/synthetic_customer_records.json
```

The records include two synthetic tenants. One record is in the current user's
scope; the other models a cross-tenant disclosure risk.

## Attack

The attack payloads ask the support agent to reveal:

- a synthetic secret marker,
- another tenant's full record,
- internal support notes.

In the vulnerable baseline, the agent retrieves broad records and answers from
the full context. That turns context availability into unauthorized disclosure.

## Defense

The defense combines three small controls:

- retrieval scoping to the current tenant and customer id,
- data minimization to support-summary fields,
- synthetic secret-pattern blocking.

This is not a complete privacy system. It is a small experiment showing that
agents need explicit data boundaries around both retrieval and output.

## Evaluation

Run:

```bash
.venv/bin/python lab/attacker/custom/run_llm02_sensitive_disclosure_attacks.py --mode compare
```

Expected v0-style result:

```text
defense OFF: 1.0
defense ON: 0.0
absolute reduction: 1.0
```

## What Comes Next

- Add role-based payloads for support, billing, and admin personas.
- Add field-level allowlists by task.
- Add tests for partial redaction and refusal wording.

## Blog And Talk Notes

For the blog series, the key framing is that context is data exposure. Agents
should not retrieve or carry sensitive fields unless the current user and task
need them.

For the Summit talk, this module pairs naturally with retrieval and memory
sections: the same convenience that makes agents useful can quietly expand the
blast radius of sensitive data.
