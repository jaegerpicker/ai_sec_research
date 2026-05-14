"""Spotlighting defense for the v0 vulnerable RAG agent.

Spotlighting is a boundary-marker defense (Microsoft Research, 2024) that
labels content from untrusted sources so an agent treats it as data, not
instructions. This v0 implementation wraps every non-trusted retrieved
document in <<UNTRUSTED>>...<</UNTRUSTED>> delimiters and sets a
``spotlighted`` flag. The agent's action selector ignores instruction-like
triggers from spotlighted documents.

The defense is intentionally minimal. Production spotlighting also datamarks
token boundaries or base64-encodes untrusted content; for v0 the delimiter
plus action-scope restriction is enough to demonstrate the OFF vs ON eval
delta.
"""
from typing import Iterable

UNTRUSTED_OPEN = "<<UNTRUSTED>>"
UNTRUSTED_CLOSE = "<</UNTRUSTED>>"
TRUSTED = "trusted"


def apply_spotlighting(documents: Iterable[dict]) -> list[dict]:
    out: list[dict] = []
    for doc in documents:
        if doc.get("trust") == TRUSTED:
            out.append({**doc, "spotlighted": False})
        else:
            marked = f"{UNTRUSTED_OPEN}\n{doc['content']}\n{UNTRUSTED_CLOSE}"
            out.append({**doc, "spotlighted": True, "content": marked})
    return out
