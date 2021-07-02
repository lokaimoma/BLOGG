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
        return {
            "title": self.title,
            "body": self.body,
            "created_date": self.created_date.__str__(),
            "last_update": self.last_updated.__str__(),
            "user_id": self.user_id
        }
