from pydantic import BaseModel


class UserDomain(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str
    email: str


def map_UserDomain_to_UserBaseModel(userDomain: UserDomain):
    return {
        "username": userDomain.username,
        "email": userDomain.email
    }
