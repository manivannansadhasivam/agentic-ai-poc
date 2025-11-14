from fastapi import FastAPI
import uvicorn

app = FastAPI(title="agentic-ai-poc")

@app.get("/agentic-ai")
def read_root():
    # Updated per JIRA-1: should return the specified welcome message
    return "Hellow, Welcome to Agentic AI World"

# Entry point helper for uvicorn;
# You can still run: uvicorn main:app --port 9000
if __name__ == "__main__":
    uvicorn.run(app)
