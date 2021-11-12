"""
Date: 9 nov 2021
Time: 9.45 am
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is the main source file of the Small Proprietary Original Project OnSurf.
File content description: This file is composed of classes, These classes are BaseModels with pydantic to use object.
For safety reasons it is easier to use a BaseModel than to check values from a dictionary.
Theses classes limits the entries we can input in the SPOP database, which is a noSQL database
"""
from typing import Dict, Optional

from pydantic import BaseModel




class User(BaseModel):
    username: str
    hash_password: str
    locations: Dict[str, Location] = {}

    def add_location(self, location: Location, location_name: str):
        if location_name in self.locations:
            print(f"{location_name} already exists")
        self.locations[location_name] = location


class UserTable(BaseModel):
    __root__: Dict[str, User]

    def add(self, user: User):
        if user.username in self.__root__:
            print(f"{user.username} already exists")
        self.__root__[user.username] = user

    def save(self):
        with open("db/user.json", "w") as fp:
            fp.write(self.json())

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, username: str):
        if username not in self.__root__:
            print(f"{username} does not exists")
        return self.__root__[username]


USER_TABLE = UserTable.parse_file("db/user.json")
