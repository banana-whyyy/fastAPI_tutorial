# Описание того, как выглядит JSON, который приходит и уходит через API
from pydantic import BaseModel, Field, ConfigDict



class AuthorBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Author Name")


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id: int = Field(..., description="Unique author ID")
    model_config = ConfigDict(from_attributes=True)


class AuthorUpdate(AuthorBase):
    name: str | None = None

