import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"


class LabScaffoldTest(unittest.TestCase):
    def test_v0_lab_structure_exists(self):
        expected_paths = [
            LAB / "README.md",
            LAB / "docker-compose.yml",
            LAB / "vulnerable-agents" / "injection-via-rag",
            LAB / "attacker" / "payloads",
            LAB / "attacker" / "custom",
            LAB / "evals" / "results",
            LAB / "defenses" / "spotlighting",
            LAB / "proxy" / "logs",
            LAB / "writeups",
        ]

        missing = [str(path.relative_to(ROOT)) for path in expected_paths if not path.exists()]

        self.assertEqual([], missing)

    def test_v0_readme_documents_goal_and_safety_boundaries(self):
        self.assertTrue((LAB / "README.md").exists(), "lab/README.md should exist")
        readme = (LAB / "README.md").read_text(encoding="utf-8")

        self.assertIn("v0", readme)
        self.assertIn("indirect prompt injection", readme)
        self.assertIn("No real credentials", readme)
        self.assertIn("No host network mode", readme)
        self.assertIn("docker compose", readme)

    def test_docker_compose_declares_initial_lab_services(self):
        self.assertTrue((LAB / "docker-compose.yml").exists(), "lab/docker-compose.yml should exist")
        compose = (LAB / "docker-compose.yml").read_text(encoding="utf-8")

        self.assertIn("vulnerable-rag:", compose)
        self.assertIn("egress-proxy:", compose)
        self.assertIn("redteam-lab:", compose)
        self.assertIn('"127.0.0.1:8000:8000"', compose)
        self.assertIn("dockerfile: lab/vulnerable-agents/injection-via-rag/Dockerfile", compose)

    def test_package_json_exposes_lab_test_command(self):
        package_json = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))

        self.assertEqual(
            "node scripts/run-lab-tests.mjs",
            package_json["scripts"].get("test:lab"),
        )


if __name__ == "__main__":
    unittest.main()
