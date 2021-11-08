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
