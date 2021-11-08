import uvicorn
from fastapi import FastAPI, Body, Depends
from starlette.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# intialize web app / pi
from app.db import crud
from app.db.tables import Location
from app.security.security import verify_credentials

app = FastAPI()
security = HTTPBasic()

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


@app.post("/add/location", response_model=bool)
def add_location(credentials: HTTPBasicCredentials = Depends(security),
                 longitude: float = Body(..., min=-180, max=180),
                 latitude: float = Body(..., min=-90, max=90),
                 location_name: str = Body(..., min_length=1)):
    verify_credentials(credentials.username, credentials.password)
    location = Location(latitude=latitude, longitude=longitude)
    crud.add_location(credentials.username, location, location_name)
    return True


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
