from typing import Dict, Union

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
