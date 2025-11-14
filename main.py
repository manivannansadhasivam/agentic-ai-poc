from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="agentic-ai-poc")

@app.get("/agentic-ai")
def read_root():
    # fix(JIRA-3): Return a structured JSON payload for extensibility and proper JSON media type instead of a raw string.
    return JSONResponse(content={"message": "Hello, Welcome to Agentic AI World"})

# Entry point helper for uvicorn;
# You can still run: uvicorn main:app --port 9000
if __name__ == "__main__":
    uvicorn.run(app)
