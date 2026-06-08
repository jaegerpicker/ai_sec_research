import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TALK_DIR = ROOT / "talks" / "summit-owasp-llm-top-10"
RUNBOOK_PATH = TALK_DIR / "demo-runbook.md"
PREFLIGHT_PATH = TALK_DIR / "demo-preflight.py"
PYTHON = ROOT / ".venv" / "bin" / "python"


class TalkDemoPreflightTest(unittest.TestCase):
    def test_live_demo_summary_reads_the_fresh_rehearsal_result(self):
        runbook = RUNBOOK_PATH.read_text(encoding="utf-8")

        self.assertIn('open("/tmp/llm01-compare-rehearsal.json")', runbook)

    def test_preflight_verifies_the_expected_measured_delta(self):
        completed = subprocess.run(
            [str(PYTHON), str(PREFLIGHT_PATH)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("defense off: 3/3 ASR 1.0", completed.stdout)
        self.assertIn("defense on: 0/3 ASR 0.0", completed.stdout)
        self.assertIn("absolute reduction: 1.0", completed.stdout)
        self.assertIn("preflight: PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
