import sqlalchemy as sa
from . import SQLAlchemyBase
from src.domain_logic.user_domain import UserDomain
from src.util.security.password_util import hash_password


class User(SQLAlchemyBase):
    __tablename__ = "users"
    id: int = sa.Column(sa.Integer, pirmary_key=True, autoincrement=True)
    username: str = sa.Column(sa.String, unique=True,
                              nullable=False, index=True)
    email: str = sa.Column(sa.String, unique=True, index=True, nullable=False)
    password: str = sa.Column(sa.String, nullable=False)

    def __init__(self, userDomain: UserDomain):
        self.username = userDomain.username
        self.email = userDomain.email
        self.password = hash_password(password=userDomain.password)
