from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/dashboard")
def dashboard(
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[str | None, Header()] = None,

    ):
    return {"access_token:": access_token, "user_role:": user_role}