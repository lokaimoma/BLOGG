from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from . import SQLAlchemyBase
from src.domain_logic.blog_domain import BlogDomain


class Blog(SQLAlchemyBase):
    __tablename__ = "blogs"
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String, nullable=False)
    body: str = sa.Column(sa.String)
    created_date: datetime = sa.Column(sa.DateTime)
    last_updated: datetime = sa.Column(sa.DateTime)
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = relationship("User", back_populates="blogs")
    engagements: list = relationship(
        "Engagement", back_populates="blog", cascade="all, delete-orphan")

    def __init__(self, blog_domain: BlogDomain):
        self.title = blog_domain.title
        self.body = blog_domain.body
        self.created_date = blog_domain.created_date
        self.last_updated = blog_domain.last_updated
        self.user_id = blog_domain.user_id

    def to_dict(self):
        return {
            "title": self.title,
            "body": self.body,
            "created_date": self.created_date.__str__(),
            "last_updated": self.last_updated.__str__(),
            "user_id": self.user_id
        }
