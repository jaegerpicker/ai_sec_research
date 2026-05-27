import importlib.util
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
MODULE = LAB / "owasp-llm-top-10" / "llm07-system-prompt-leakage"
TARGET = LAB / "vulnerable-agents" / "system-prompt-leakage-agent"
RUNNER_PATH = LAB / "attacker" / "custom" / "run_llm07_prompt_leakage_attacks.py"
PAYLOADS_PATH = LAB / "attacker" / "payloads" / "system_prompt_leakage.json"
WRITEUP = LAB / "writeups" / "007-system-prompt-leakage.md"
PYTHON = ROOT / ".venv" / "bin" / "python"


def load_runner_module():
    spec = importlib.util.spec_from_file_location("run_llm07_prompt_leakage_attacks", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Llm07SystemPromptLeakageLabTest(unittest.TestCase):
    def test_module_artifacts_exist(self):
        expected_paths = [
            MODULE / "README.md",
            TARGET / "app.py",
            RUNNER_PATH,
            PAYLOADS_PATH,
            WRITEUP,
        ]

        missing = [str(path.relative_to(ROOT)) for path in expected_paths if not path.exists()]

        self.assertEqual([], missing)

    def test_module_readme_documents_prompt_leakage_and_safety(self):
        readme = (MODULE / "README.md").read_text(encoding="utf-8")

        expected_text = [
            "LLM07:2025 System Prompt Leakage",
            "synthetic hidden instructions",
            "prompt-only secret",
            "Use synthetic prompt content only",
            "No real secrets",
            "defense OFF",
            "defense ON",
        ]

        missing = [text for text in expected_text if text not in readme]

        self.assertEqual([], missing)

    def test_payload_library_models_direct_and_indirect_leakage(self):
        payloads = json.loads(PAYLOADS_PATH.read_text(encoding="utf-8"))

        self.assertGreaterEqual(len(payloads), 3)
        self.assertTrue(all("id" in payload for payload in payloads))
        self.assertTrue(all("message" in payload for payload in payloads))
        self.assertEqual(
            {"leak_system_prompt", "leak_routing_rules", "leak_prompt_secret"},
            {payload["expected_leak"] for payload in payloads},
        )

    def test_runner_reports_baseline_and_defense_delta(self):
        runner = load_runner_module()

        report = runner.run_comparison()

        self.assertEqual("llm07-system-prompt-leakage-defense-comparison", report["suite"])
        self.assertEqual("LLM07:2025", report["metadata"]["owasp_id"])
        self.assertEqual("System Prompt Leakage", report["metadata"]["owasp_name"])
        self.assertEqual(1.0, report["defense_off"]["leakage_success_rate"])
        self.assertEqual(0.0, report["defense_on"]["leakage_success_rate"])
        self.assertEqual(1.0, report["delta"]["absolute_reduction"])

    def test_cli_compare_writes_json_report(self):
        output_path = ROOT / "lab" / "evals" / "results" / "llm07-prompt-leakage-latest.json"
        if output_path.exists():
            output_path.unlink()

        completed = subprocess.run(
            [str(PYTHON), str(RUNNER_PATH), "--mode", "compare", "--output", str(output_path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertTrue(output_path.exists(), "runner should write JSON results")

        report = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual("LLM07:2025", report["metadata"]["owasp_id"])
        self.assertEqual(1.0, report["delta"]["absolute_reduction"])


if __name__ == "__main__":
    unittest.main()
