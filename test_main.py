from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    resp = client.get("/agentic-ai")
    assert resp.status_code == 200
    assert resp.json() == "Hello, World!"