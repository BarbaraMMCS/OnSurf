import uvicorn
from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse

#intialize web app / pi
from app.db import crud

app = FastAPI()

# Redirects base url to docs goto /redoc for fancy documentation 
@app.get("/")
def main():
    return RedirectResponse(url="/docs")


# GET request for Name Read name is passed in url rather than json 
@app.post("/create/user", response_model=bool)
def create_user(username: str = Body(..., min_length=1),
                password: str = Body(..., min_length=6)):
    crud.create_user(username=username, password=password)
    return True


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
