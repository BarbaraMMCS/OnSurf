import json
from typing import Dict

from fastapi import HTTPException
from pydantic import BaseModel


class User(BaseModel):
    username: str
    hash_password: str

class UserTable(BaseModel):
    __root__: Dict[str, User]

    def add(self, user: User):
        if user.username in self.__root__:
            raise HTTPException(status_code=500, detail="User already exists")
        self.__root__[user.username] = user

    def save(self):
        with open("db/user.json", "w") as fp:
            fp.write(self.json())

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, username: str):
        return self.__root__[username]

USER_TABLE = UserTable.parse_file("db/user.json")
