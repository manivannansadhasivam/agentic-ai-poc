from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="agentic-ai-poc")

@app.get("/agentic-ai")
def read_root():
    # fix(JIRA-3): Correct welcome message per Jira; keep structured JSON for future extensibility.
    # Previous response: {"message": "Hello, Welcome to Agentic AI World"}
    # Root cause: Hardcoded incorrect greeting string not matching product spec.
    return JSONResponse(content={"message": "Hello World"})

# Entry point helper for uvicorn;
# You can still run: uvicorn main:app --port 9000
if __name__ == "__main__":
    uvicorn.run(app)
