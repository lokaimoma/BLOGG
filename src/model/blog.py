from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.orm import relation
from . import SQLAlchemyBase
from src.domain_logic.blog_domain import BlogDomain


class Blog(SQLAlchemyBase):
    __tablename__ = "blogs"
    id: str = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String, nullable=False)
    body: str = sa.Column(sa.String)
    created_data: datetime = sa.Column(sa.DateTime)
    last_updated: datetime = sa.Column(sa.DateTime)
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = relation("User")

    
    def __init__(self, blogDomain: BlogDomain):
        self.title = blogDomain.title
        self.body = blogDomain.body
        self.created_data = blogDomain.created_date
        self.last_updated = blogDomain.last_updated
        self.user_id = blogDomain.user_id