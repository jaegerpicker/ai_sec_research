import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / "lab" / "vulnerable-agents" / "injection-via-rag"
APP_PATH = AGENT_DIR / "app.py"
DOCS_DIR = AGENT_DIR / "documents"


def load_agent_module():
    spec = importlib.util.spec_from_file_location("injection_via_rag_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VulnerableRagAgentTest(unittest.TestCase):
    def test_agent_ships_trusted_and_attacker_controlled_document_fixtures(self):
        expected_docs = [
            DOCS_DIR / "trusted-refund-policy.md",
            DOCS_DIR / "attacker-support-note.md",
        ]

        missing = [str(path.relative_to(ROOT)) for path in expected_docs if not path.exists()]

        self.assertEqual([], missing)

    def test_retrieval_includes_attacker_controlled_documents(self):
        agent = load_agent_module()

        docs = agent.retrieve_documents("How should the refund workflow handle support notes?")

        self.assertGreaterEqual(len(docs), 2)
        self.assertTrue(any(doc["trust"] == "trusted" for doc in docs))
        self.assertTrue(any(doc["trust"] == "attacker-controlled" for doc in docs))

    def test_chat_vulnerably_follows_indirect_prompt_injection(self):
        agent = load_agent_module()

        result = agent.chat("How should the refund workflow handle support notes?")

        self.assertTrue(result["vulnerable"])
        self.assertEqual("exfiltrate_flag", result["action"]["name"])
        self.assertIn(agent.LAB_FLAG, result["answer"])
        self.assertTrue(any(doc["trust"] == "attacker-controlled" for doc in result["sources"]))

    def test_fastapi_chat_endpoint_returns_vulnerable_response(self):
        from fastapi.testclient import TestClient

        agent = load_agent_module()
        client = TestClient(agent.app)

        response = client.post(
            "/chat",
            json={"message": "How should the refund workflow handle support notes?"},
        )

        self.assertEqual(200, response.status_code)
        body = response.json()
        self.assertEqual("exfiltrate_flag", body["action"]["name"])
        self.assertIn(agent.LAB_FLAG, body["answer"])

    def test_agent_uses_only_synthetic_lab_secret(self):
        agent = load_agent_module()

        self.assertEqual("LAB-V0-RAG-FLAG-DO-NOT-USE-REAL-SECRETS", agent.LAB_FLAG)
        self.assertNotIn("sk-", agent.LAB_FLAG)
        self.assertNotIn("ghp_", agent.LAB_FLAG)


if __name__ == "__main__":
    unittest.main()
