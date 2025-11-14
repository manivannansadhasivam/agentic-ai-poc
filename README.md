# agentic-ai-poc

Minimal FastAPI application with a single GET endpoint returning `hello world`.

## Requirements
Python 3.10+ recommended.

## Installation
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Run
```powershell
uvicorn main:app --reload --port 8000
```
Visit: http://127.0.0.1:8000/

## Test
```powershell
pytest -q
```

## Endpoint
GET `/` -> `{ "message": "hello world" }`

## Next Steps (optional)
- Add more endpoints
- Containerize with Docker
- CI workflow for tests
