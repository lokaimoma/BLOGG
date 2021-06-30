from typing import Optional
from pydantic import BaseModel


class EngagementDomain(BaseModel):
    blog_id: int
    user_id: int
    isLiked: Optional[bool] = False
