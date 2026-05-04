import os
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from pydantic import computed_field

class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original_url: str
    short_name: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    @computed_field
    @property
    def short_url(self) -> str:
        base = os.getenv("BASE_URL", "http://localhost:8080/r/")
        return f"{base}{self.short_name}"