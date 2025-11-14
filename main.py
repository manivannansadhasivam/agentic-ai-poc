from fastapi import FastAPI
import uvicorn

app = FastAPI(title="agentic-ai-poc")

@app.get("/")
def read_root():
    return "Hello, World!"

# Entry point helper for uvicorn; defaults to port 9000
# You can still run: uvicorn main:app --reload --port 9000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000, reload=True)
