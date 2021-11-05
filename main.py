import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

#intialize web app / pi
app = FastAPI()

# Redirects base url to docs goto /redoc for fancy documentation 
@app.get("/")
def main():
    return RedirectResponse(url="/docs")


# GET request for Name Read name is passed in url rather than json 
@app.get("/api/read/{name}", response_model=str)
def get_name(name:str):
    return name


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
