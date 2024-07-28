from typing import Annotated
from fastapi import FastAPI, Header, Request

app = FastAPI()

@app.get("/dashboard")
def dashboard(
    request: Request,
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[str | None, Header()] = None,
    ):
    print(request.headers)
    return {"access_token:": access_token, "user_role:": user_role}