from fastapi import FastAPI

app = FastAPI(title="agentic-ai-poc")

@app.get("/")
def read_root():
    return {"message": "hello world"}

# Entry point helper for uvicorn if needed
# Run: uvicorn main:app --reload
