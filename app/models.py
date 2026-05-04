from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original_url: str
    short_name: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)