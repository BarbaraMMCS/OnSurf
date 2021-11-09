"""
Date: 9 nov 2021
Time: 9.45 am
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is the main source file of the Small Proprietary Original Project OnSurf.
File content description: This file is a security module, it checks the different passwords, and it hashes the password.
"""
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
