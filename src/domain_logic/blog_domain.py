from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BlogDomain(BaseModel):
    title: str
    body: str
    created_date: Optional[datetime]
    last_updated: Optional[datetime]
    user_id: int
