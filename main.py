"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is one of the main source files of
the Small Proprietary Original Project OnSurf.
File content description: This file is the main source file of the project.

This file contains the main functionalities to run OnSurf: run_on_surf, which is
the main program loop.
Then this file has the user functions: login, logout, hash_password, create
and delete user.
As well as welcome_menu, admin_menu, base_user_menu and user_menu.
We have the object USER_TABLE in this file. It is an object from the class UserTable.
USER_TABLE is an object needed to store a user's credentials, userspace
and weather reports.
Lastly, we have a variable CURRENT_USER that is needed to log as a user or an admin.
"""
import hashlib
from datetime import datetime
from typing import Optional

from app.DataModels import Location, CoordinatesGPS
from app.User import User
from app.UserTable import UserTable
from app.print_service import print_OnSurf, print_welcome_menu, print_admin_menu, \
    print_base_user_menu, print_user_menu


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('UTF-8')).hexdigest()


def login(username: str, password: str) -> bool:
    global CURRENT_USER
    user = USER_TABLE[username]
    if user.hash_password == hash_password(password):
        CURRENT_USER = user
        return True
    return False


def logout() -> bool:
    global CURRENT_USER
    CURRENT_USER = None
    return True


def run_on_surf():
    is_on = True
    print_OnSurf()
    print_welcome_menu()
    while is_on:
        command = str(input("Press any key to see MENU or command >"))
        if command in {"q", "quit"}:
            is_on = False
            continue

        if CURRENT_USER is None:
            print_welcome_menu()
            welcome_menu(command)
        else:
            if CURRENT_USER.is_admin:
                print_admin_menu()
                admin_menu(command)
            elif not CURRENT_USER.is_admin:
                print_base_user_menu()
                base_user_menu(command)
            print_user_menu()
            user_menu(command)


def oe_delete_user(username: str) -> bool:
    return USER_TABLE.delete(username)


def oe_create_base_user(username: str, password: str) -> bool:
    user = User(username=username, hash_password=hash_password(password))
    USER_TABLE.add(user)
    return True


def admin_menu(command: str) -> None:
    if command == "delete user":
        oe_delete_user(input("The username >"))


def welcome_menu(command: str) -> None:
    if command == "login":
        login(input("Your username >"), input("Your password >"))
    elif command == "create user":
        oe_create_base_user(input("Your username >"), input("Your password >"))


def base_user_menu(command: str) -> None:
    if command == "add location":
        location = Location(location_name=input("Location name >"),
                            coordinates=CoordinatesGPS(
                                latitude=float(input("latitude [-90, 90] > ")),
                                longitude=float(input("longitude [-180, 180] > "))
                            ))
        CURRENT_USER.add_surf_location(location)
        USER_TABLE.save()
    if command == "remove location":
        location_name = input("Location name >")
        CURRENT_USER.remove_surf_location(location_name)
        USER_TABLE.save()
    if command == "display userspace":
        CURRENT_USER.display_userspace()
    if command == "get weather":
        now = datetime.now()
        time = datetime(now.year, now.month, int(input("2021-11-day, day >")),
                        int(input("24h format hour >")))
        CURRENT_USER.get_weather(time)
        USER_TABLE.save()
    if command == "best surf spot":
        CURRENT_USER.ask_on_surf_the_best_spot()


def user_menu(command: str) -> None:
    if command == "logout":
        logout()


CURRENT_USER: Optional[User] = None
USER_TABLE = UserTable.parse_file("db/user.json")

if __name__ == "__main__":
    run_on_surf()
