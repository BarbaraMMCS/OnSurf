import hashlib

from app.db.tables import User, USER_TABLE


def create_user(username: str, password: str):
    hash_password = hashlib.sha256(password.encode('UTF-8')).hexdigest()
    user = User(username=username, hash_password=hash_password)
    USER_TABLE.add(user)
    USER_TABLE.save()

def get_user(username: str):
    return USER_TABLE[username]
