from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agentic_ai_welcome_message():
    resp = client.get("/agentic-ai")
    assert resp.status_code == 200
    # Expected message per JIRA-1 specification
    # Updated expectation per JIRA-2: spelling correction
    assert resp.json() == "Hello, Welcome to Agentic AI World"
