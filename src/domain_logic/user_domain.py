from pydantic import BaseModel


class UserDomain(BaseModel):
    username: str
    email: str
    password: str
