"""
Date: 12 nov 2021
Time: 22.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is the main source file of the Small Proprietary Original Project OnSurf.
File content description: This file the main file of the project
it contains classes and interfaces
"""

from datetime import datetime
from enum import Enum
from typing import Dict, Union, Optional

from pydantic import BaseModel, Field

from app.db.tables import USER_TABLE
from app.security.security import hash_password


class CoordinatesGPS(BaseModel):
    longitude: float = Field(..., gt=0, le=10)
    latitude: float = Field(..., gt=0, le=10)


class Location(BaseModel):
    location: str
    coordinates: Optional[CoordinatesGPS]


class CompassPoints(str, Enum):
    N = 'N'
    NE = 'NE'
    E = 'E'
    SE = 'SE'
    S = 'S'
    SW = 'SW'
    W = 'W'
    NW = 'NW'


class Weather(BaseModel):
    WindDirection: CompassPoints
    WindSpeed: int
    WaveDirection: CompassPoints
    WaveSize: float
    HighTide: datetime.time


class WeatherDatabase(BaseModel):
    locations: Dict[str, Weather] = {}


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


class Authenticated(BaseModel):
    @staticmethod
    def oe_login(self, login: str, password: str) -> bool:
        return True

    @staticmethod
    def oe_logout(self) -> bool:
        return True

    @staticmethod
    def ie_message(self, message: str) -> bool:
        return True


class User:
    username: str
    hash_password: str
    locations: WeatherDatabase

    def __init__(self):
        pass

    @staticmethod
    def oe_create_user(login: str, password: str) -> bool:
        user = User(username=login, hash_password=hash_password(password))
        USER_TABLE.add(user)
        USER_TABLE.save()
        return True

    def oe_add_surf_location(self, location: Location) -> bool:
        if location in self.locations:
            print(f"{location} already exists")
        self.locations[location] = location
        return True

    @staticmethod
    def oe_get_weather(self, time: datetime.time, date: datetime.date) -> bool:
        return True

    @staticmethod
    def oe_ask_on_surf_the_best_spot(self) -> bool:
        return True

    @staticmethod
    def oe_remove_surf_location(self, location: Union[CoordinatesGPS, str]) -> bool:
        return True

    @staticmethod
    def ie_user_created(self) -> bool:
        return True

    @staticmethod
    def ie_surf_location_added(self) -> bool:
        return True

    @staticmethod
    def ie_weather_report(self, location: Location, wind_direction: CompassPoints, wind_speed: int,
                          wave_direction: CompassPoints, wave_size: float, high_tide: datetime.time) -> bool:
        return True

    @staticmethod
    def ie_the_best_surf_spot(self, location: Location) -> bool:
        return True

    @staticmethod
    def ie_surf_location_emoved(self) -> bool:
        return True


class Administrator:
    @staticmethod
    def oe_delete_user(self, user: str) -> bool:
        return True

    @staticmethod
    def ie_user_deleted(self) -> bool:
        return True


class Creator:
    def __init__(self):
        pass

    @staticmethod
    def oe_install_system(self) -> bool:
        return True

    @staticmethod
    def oe_import_database(self, database: WeatherDatabase) -> bool:
        return True

    @staticmethod
    def ie_database_imported(self) -> bool:
        return True


def admin_menu(command: str) -> None:
    if command == "delete user":
        Administrator.oe_delete_user()
    if command == "install system":
        Creator.oe_install_system()
    if command == "import database":
        Creator.oe_import_database()


def menu(command: str) -> None:
    if command == "create user":
        User.oe_create_user()
    if command == "add location":
        User.oe_add_surf_location()
    if command == "remove location":
        User.oe_remove_surf_location()
    if command == "get weather":
        User.oe_get_weather()
    if command == "the best spot":
        User.oe_ask_on_surf_the_best_spot()


def menu_authenticate(command: str) -> bool:
    logged = False
    if command == "login":
        logged = Authenticated.oe_login()
    if command == "logout":
        logged = Authenticated.oe_logout()
    return logged


def is_admin() -> bool:
    return False


def runOnSurf():
    is_on = True
    while is_on:

        command = str(input("--Welcome to OnSurf--"))

        if command == ("q" | "quit"):
            is_on = False
            continue

        logged = menu_authenticate(command)
        while logged:
            if is_admin():
                admin_menu(command)
            else:
                menu(command)


from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float
    name: Optional[str]


USER_TABLE = UserTable.parse_file("db/user.json")

if __name__ == "__main__":
    runOnSurf()
