from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agentic_ai_welcome_message():
    resp = client.get("/agentic-ai")
    assert resp.status_code == 200
    # test(JIRA-3): Expect structured JSON object for extensibility instead of raw JSON string
    assert resp.json() == {"message": "Hello, Welcome to Agentic AI World"}
