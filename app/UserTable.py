"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files
of the Small Proprietary Original Project OnSurf.
File content description: This file a class file of the project.

This file contains the class UserTable which inherits from the class BaseModel
from the Pydantic library.
Defining a base model for UserTable allows to pass data to the object
and ensure all fields will conform to types defined in the model.

The program needs to iterate over the object UserTable's keys that do not exists yet.
These are username attributes from the object User.
Hence, the variable __root__ is used.
__root__ will function with any dictionary which contains User objects with
an attribute of type strings as key in UserTable.
The class also contains methods to add and delete users to the object UserTable
As well as one method to save the object's state as a json object.
Lastly, base functions __iter__ and __getitem__ have been overwritten.
"""
from typing import Dict

from pydantic import BaseModel

from app.User import User


class UserTable(BaseModel):
    __root__: Dict[str, User]

    def add(self, user: User) -> bool:
        if user.username in self.__root__:
            print(f"{user.username} already exists")
            return False
        self.__root__[user.username] = user
        self.save()

    def save(self):
        with open("db/user.json", "w") as fp:
            fp.write(self.json())

    def delete(self, username: str) -> bool:
        if username in self.__root__:
            del self.__root__[username]
            self.save()
            return True
        return False

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, username: str) -> User:
        if username not in self.__root__:
            print(f"{username} does not exists")
        return self.__root__[username]
