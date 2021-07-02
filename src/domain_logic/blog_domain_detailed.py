from typing import Optional

from pydantic import BaseModel

from src.domain_logic.blog_domain import BlogDomain


class BlogDomainDetail(BaseModel):
    blog: BlogDomain
    current_user_likes: Optional[bool]
    likes_count: int
    dislikes_count: int

    def to_dict(self):
        return {
            "blog": self.blog.to_dict(),
            "current_user_likes": self.current_user_likes,
            "likes_count": self.likes_count,
            "dislikes_count": self.dislikes_count
        }

