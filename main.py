from typing import Annotated
from fastapi import FastAPI, Header, Request, Response

app = FastAPI()

@app.get("/dashboard")
def dashboard(
    request: Request,
    response: Response,
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[str | None, Header()] = None,
    ):
    response.headers["user_status"] = "enabled"
    return {"access_token:": access_token, "user_role:": user_role}