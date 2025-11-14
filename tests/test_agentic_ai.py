from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agentic_ai_welcome_message():
    resp = client.get("/agentic-ai")
    assert resp.status_code == 200
    # test(JIRA-3): Updated expectation per bug fix: endpoint must return canonical greeting 'Hello World'
    # This test previously expected 'Hello, Welcome to Agentic AI World' (incorrect per Jira).
    assert resp.json() == {"message": "Hello World"}
