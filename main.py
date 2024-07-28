from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/dashboard")
def dashboard(access_token: Annotated[str, Header()]):
    return "dashboard"