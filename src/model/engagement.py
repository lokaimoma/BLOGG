import sqlalchemy as sa
from sqlalchemy.orm import relationship
from . import SQLAlchemyBase
from src.domain_logic.engagement_domain import EngagementDomain


class Engagement(SQLAlchemyBase):
    __tablename__ = "engagements"
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    blog_id: int = sa.Column(sa.Integer, sa.ForeignKey("blogs.id"))
    user_id: int = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    isLiked: bool = sa.Column(sa.Boolean)
    blog = relationship("Blog", back_populates="engagements")

    def __init__(self, engagement_domain: EngagementDomain):
        self.blog_id = engagement_domain.blog_id
        self.user_id = engagement_domain.user_id
        self.isLiked = engagement_domain.isLiked
