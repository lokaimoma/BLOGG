from pydantic import BaseModel


class UserDomain(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str
    email: str


class UserLogin(BaseModel):
    id: int
    email: str
    username: str
