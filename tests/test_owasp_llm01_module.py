import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
MODULE = LAB / "owasp-llm-top-10" / "llm01-prompt-injection"
README = MODULE / "README.md"


class OwaspLlm01ModuleTest(unittest.TestCase):
    def test_llm01_module_readme_exists(self):
        self.assertTrue(README.exists(), "LLM01 module README should exist")

    def test_llm01_module_maps_existing_v0_artifacts(self):
        readme = README.read_text(encoding="utf-8")

        expected_text = [
            "LLM01:2025 Prompt Injection",
            "indirect prompt injection",
            "lab/vulnerable-agents/injection-via-rag",
            "lab/attacker/custom/run_v0_rag_attacks.py",
            "lab/attacker/payloads/indirect_prompt_injection.json",
            "lab/defenses/spotlighting",
            "lab/evals/results/v0-rag-latest.json",
            "lab/writeups/001-injection-via-rag.md",
            "src/content/blog/breaking-agents-llm01-prompt-injection.md",
            "No third-party LLM applications",
        ]

        missing = [text for text in expected_text if text not in readme]

        self.assertEqual([], missing)

    def test_llm01_referenced_artifacts_exist(self):
        expected_paths = [
            LAB / "vulnerable-agents" / "injection-via-rag",
            LAB / "attacker" / "custom" / "run_v0_rag_attacks.py",
            LAB / "attacker" / "payloads" / "indirect_prompt_injection.json",
            LAB / "defenses" / "spotlighting",
            LAB / "evals" / "results",
            LAB / "writeups" / "001-injection-via-rag.md",
            ROOT / "src" / "content" / "blog" / "breaking-agents-llm01-prompt-injection.md",
        ]

        missing = [str(path.relative_to(ROOT)) for path in expected_paths if not path.exists()]

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
