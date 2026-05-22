from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Lab 1 setup complete"}