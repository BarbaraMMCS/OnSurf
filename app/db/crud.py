"""
Date: 9 nov 2021
Time: 9.45 am
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is the main source file of the Small Proprietary Original Project OnSurf.
File content description: This file is an interface module, this interface interacts with the database.
If the database changes only this file needs to be modified.
The main functions are the basic Create, Read, Update and Delete.
"""

from app.db.tables import User, USER_TABLE, Location
from app.security.security import hash_password


def create_user(username: str, password: str):
    user = User(username=username, hash_password=hash_password(password))
    USER_TABLE.add(user)
    USER_TABLE.save()

def get_user(username: str):
    return USER_TABLE[username]

def add_location(username: str, location: Location, location_name: str):
    USER_TABLE[username].add_location(location, location_name)
    USER_TABLE.save()
