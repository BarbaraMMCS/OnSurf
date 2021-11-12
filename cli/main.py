from pydantic import BaseModel
from typing import Dict


class Location(BaseModel):
    AdtLocation: str


class Weather(BaseModel):
    AdtWindDirection: str
    AdtWindSpeed: int
    AdtWaveDirection: str
    AdtWaveSize: float
    AdtHighTide: [int, int, int]


class WeatherDatabase(BaseModel):
    AdtWeather: Dict[Location, Weather] = {}


class Authenticated:
    AdtLogin: str
    AdtPassword: str

    def __init__(self, ALogin: dtLogin, APassword: dtLogin):

    def oeLogin(self, ALogin: dtLogin, APassword: dtPassword) -> bool:
        pass

    def oeLogout(self) -> bool:
        pass

    def ieMessage(self, AMessage: ptString) -> bool:
        pass


class User(Authenticated):
    AdtLocations: WeatherDatabase

    def __init__(self, ALogin: dtLogin, APassword: dtLogin):
        super().__init__(ALogin, APassword)

    def oeCreateUser(self, ALogin: dtLogin, APassword: dtPassword) -> bool:
        pass

    def oeAddSurfLocation(self, ALocation: dtLocation) -> bool:
        pass

    def oeGetWeather(self, ATime: dtTime, ADate: dtDate) -> bool:
        pass

    def oeAskOnSurfTheBestSpot(self) -> bool:
        pass

    def oeRemoveSurfLocation(self, ALocation: dtLocation) -> bool:
        pass

    def ieUserCreated(self) -> bool:
        pass

    def ieSurfLocationAdded(self) -> bool:
        pass

    def ieWeatherReport(self, ALocation: dtLocation, AWindDirection: dtWindDirection, AWindSpeed: dtWindSpeed,
                        AWaveDirection: dtWaveDirection, AWaveSize: dtWaveSize, AHighTide: dtHighTide) -> bool:
        pass

    def ieTheBestSurfSpot(self, ALocation: dtLocation) -> bool:
        pass

    def ieSurfLocationRemoved(self) -> bool:
        pass


class Administrator(Authenticated):

    def __init__(self, ALogin: dtLogin, APassword: dtLogin):
        super().__init__(ALogin, APassword)

    def oeDeleteUser(self, AUserID: dtUserID) -> bool:
        pass

    def ieUserDeleted(self) -> bool:
        pass


class Creator:
    def __init__(self):
        pass

    def oeInstallSystem(self) -> bool:
        pass

    def oeImportDatabase(self, ADatabase: dtDatabase) -> bool:
        pass

    def ieDataBaseImported(self) -> bool:
        pass


def admin_menu(command: str) -> None:
    if command == "delete user":
        oeDeleteUser()
    if command == "install system":
        oeInstallSystem()
    if command == "import database":
        oeImportDatabase()


def menu(command: str) -> None:
    if command == "create user":
        oeCreateUser()
    if command == "add location":
        oeAddSurfLocation()
    if command == "get weather":
        oeGetWeather()
    if command == "the best spot":
        oeAskOnSurfTheBestSpot()
    if command == "remove location":
        oeRemoveSurfLocation()


def menu_authenticate(command: str) -> bool:
    logged = False
    if command == "login":
        logged = oeLogin()
    if command == "logout":
        logged = oeLogout()
    return logged


def runOnSurf():
    is_on = True
    while is_on:

        command = str(input("--Welcome to OnSurf--"))

        if command == ("q" | "quit"):
            is_on = False
            continue

        logged = menu_authenticate(command)
        while logged:
            if logged == "admin":
                admin_menu(command)
            else:
                menu(command)


if __name__ == "__main__":
    runOnSurf()
