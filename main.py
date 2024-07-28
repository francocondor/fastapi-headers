from fastapi import FastAPI

app = FastAPI()

@app.get("/dashboard")
def dashboard():
    return "dashboard"