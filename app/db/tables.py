from typing import Dict, Optional

from fastapi import HTTPException
from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float
    name: Optional[str]


class User(BaseModel):
    username: str
    hash_password: str
    locations: Dict[str, Location] = {}

    def add_location(self, location: Location, location_name: str):
        if location_name in self.locations:
            raise HTTPException(status_code=500, detail=f"{location_name} already exists")
        self.locations[location_name] = location


class UserTable(BaseModel):
    __root__: Dict[str, User]

    def add(self, user: User):
        if user.username in self.__root__:
            raise HTTPException(status_code=500, detail=f"{user.username} already exists")
        self.__root__[user.username] = user

    def save(self):
        with open("db/user.json", "w") as fp:
            fp.write(self.json())

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, username: str):
        if username not in self.__root__:
            raise HTTPException(status_code=500, detail=f"{username} does not exists")
        return self.__root__[username]


USER_TABLE = UserTable.parse_file("db/user.json")
