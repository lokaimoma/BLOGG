import sqlalchemy as sa
from . import SQLAlchemyBase
from src.domain_logic.engagement_domain import EngagementDomain


class Engagement(SQLAlchemyBase):
    __tablename__ = "engagements"
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    blog_id: int = sa.Column(sa.Integer, sa.ForeignKey("blogs.id"))
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    isLiked: bool = sa.Column(sa.Boolean)
    isDisLiked: bool = sa.Column(sa.Boolean)


    def __init__(self, engagementDomain: EngagementDomain):
        self.blog_id = engagementDomain.blog_id
        self.user_id = engagementDomain.user_id
        self.isLiked = engagementDomain.isLiked
        self.isDisLiked = engagementDomain.isDisliked