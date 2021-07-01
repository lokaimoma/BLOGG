from typing import Optional

from pydantic import BaseModel

from src.domain_logic.blog_domain import BlogDomain


class BlogDomainDetail(BaseModel):
    blog: BlogDomain
    current_user_likes: Optional[bool]
    likes_count: int
    dislikes_count: int

    def to_dict(self):
        return self.__dict__

