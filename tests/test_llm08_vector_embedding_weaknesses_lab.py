import importlib.util
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
MODULE = LAB / "owasp-llm-top-10" / "llm08-vector-embedding-weaknesses"
TARGET = LAB / "vulnerable-agents" / "vector-neighbor-confusion"
RUNNER_PATH = LAB / "attacker" / "custom" / "run_llm08_vector_attacks.py"
PAYLOADS_PATH = LAB / "attacker" / "payloads" / "vector_embedding_weaknesses.json"
WRITEUP = LAB / "writeups" / "008-vector-embedding-weaknesses.md"
PYTHON = ROOT / ".venv" / "bin" / "python"


def load_runner_module():
    spec = importlib.util.spec_from_file_location("run_llm08_vector_attacks", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Llm08VectorEmbeddingWeaknessesLabTest(unittest.TestCase):
    def test_module_artifacts_exist(self):
        expected_paths = [
            MODULE / "README.md",
            TARGET / "app.py",
            TARGET / "documents" / "trusted-policy.md",
            TARGET / "documents" / "adversarial-neighbor.md",
            TARGET / "documents" / "duplicate-poison.md",
            RUNNER_PATH,
            PAYLOADS_PATH,
            WRITEUP,
        ]

        missing = [str(path.relative_to(ROOT)) for path in expected_paths if not path.exists()]

        self.assertEqual([], missing)

    def test_module_readme_documents_retrieval_weakness_and_safety(self):
        readme = (MODULE / "README.md").read_text(encoding="utf-8")

        expected_text = [
            "LLM08:2025 Vector and Embedding Weaknesses",
            "adversarially similar",
            "malicious-neighbor selection",
            "synthetic documents",
            "local retrieval only",
            "defense OFF",
            "defense ON",
        ]

        missing = [text for text in expected_text if text not in readme]

        self.assertEqual([], missing)

    def test_payload_library_models_retrieval_collision_behavior(self):
        payloads = json.loads(PAYLOADS_PATH.read_text(encoding="utf-8"))

        self.assertGreaterEqual(len(payloads), 3)
        self.assertTrue(all("id" in payload for payload in payloads))
        self.assertTrue(all("message" in payload for payload in payloads))
        self.assertTrue(all(payload["expected_selection"] == "malicious_neighbor" for payload in payloads))

    def test_runner_reports_baseline_and_defense_delta(self):
        runner = load_runner_module()

        report = runner.run_comparison()

        self.assertEqual("llm08-vector-embedding-weaknesses-defense-comparison", report["suite"])
        self.assertEqual("LLM08:2025", report["metadata"]["owasp_id"])
        self.assertEqual("Vector and Embedding Weaknesses", report["metadata"]["owasp_name"])
        self.assertEqual(1.0, report["defense_off"]["retrieval_attack_success_rate"])
        self.assertEqual(0.0, report["defense_on"]["retrieval_attack_success_rate"])
        self.assertEqual(1.0, report["delta"]["absolute_reduction"])

    def test_cli_compare_writes_json_report(self):
        output_path = ROOT / "lab" / "evals" / "results" / "llm08-vector-latest.json"
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
        self.assertEqual("LLM08:2025", report["metadata"]["owasp_id"])
        self.assertEqual(1.0, report["delta"]["absolute_reduction"])


if __name__ == "__main__":
    unittest.main()
