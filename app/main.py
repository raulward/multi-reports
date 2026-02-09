from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def hello_world():
    return {"status": "HEALTH (200 - OK)"}

@app.get("/")
def root_site():
    return {"status": "ROOT (200 - OK)"}