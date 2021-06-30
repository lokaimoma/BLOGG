from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BlogDomain(BaseModel):
    title: str
    body: str
    created_date: Optional[datetime] = datetime.now()
    last_updated: Optional[datetime] = datetime.now()
    user_id: int

    def to_dict(self):
        return self.__dict__
