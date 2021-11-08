import hashlib

from fastapi import HTTPException
from starlette import status

from app.db import crud


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('UTF-8')).hexdigest()


def verify_credentials(username: str, password: str):
    user = crud.get_user(username)
    if hash_password(password) == user.hash_password:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
