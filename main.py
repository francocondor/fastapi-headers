from typing import Annotated
from fastapi import FastAPI, Header, Request, Response, Depends

app = FastAPI()

def get_headers(        
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[list[str] | None, Header()] = None,
):
    return {"access_token": access_token, "user_role": user_role}

@app.get("/dashboard")
def dashboard(headers: Annotated[dict, Depends(get_headers)]):
    return {"access_token": headers["access_token"], "user_role": headers["user_role"]}