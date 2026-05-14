import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRITEUP = ROOT / "lab" / "writeups" / "001-injection-via-rag.md"


def read_writeup() -> str:
    if not WRITEUP.exists():
        raise AssertionError("v0 RAG writeup should exist")
    return WRITEUP.read_text(encoding="utf-8")


class V0WriteupTest(unittest.TestCase):
    def test_v0_writeup_exists(self):
        self.assertTrue(WRITEUP.exists(), "v0 RAG writeup should exist")

    def test_v0_writeup_covers_required_sections(self):
        text = read_writeup()

        required_headings = [
            "# v0: Indirect Prompt Injection via RAG",
            "## Architecture",
            "## Safety Boundaries",
            "## Attack",
            "## Evaluation",
            "## Defense: Spotlighting",
            "## Reproduce",
            "## What Comes Next",
        ]

        missing = [heading for heading in required_headings if heading not in text]

        self.assertEqual([], missing)

    def test_v0_writeup_includes_reproducible_commands_and_results(self):
        text = read_writeup()

        expected_snippets = [
            "python3 -m venv .venv",
            ".venv/bin/python -m pip install -r lab/requirements.txt",
            "npm run test:lab",
            ".venv/bin/python lab/attacker/custom/run_v0_rag_attacks.py --mode compare",
            "docker compose -f lab/docker-compose.yml up vulnerable-rag",
            "attack_success_rate",
            "defense OFF: 1.0",
            "defense ON: 0.0",
            "absolute reduction: 1.0",
        ]

        missing = [snippet for snippet in expected_snippets if snippet not in text]

        self.assertEqual([], missing)

    def test_v0_writeup_keeps_scope_to_owned_lab_targets(self):
        text = read_writeup()

        self.assertIn("owned local lab target", text)
        self.assertIn("No third-party LLM applications were tested", text)
        self.assertIn("LAB-V0-RAG-FLAG-DO-NOT-USE-REAL-SECRETS", text)


if __name__ == "__main__":
    unittest.main()
