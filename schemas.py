from pydantic import BaseModel, constr
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    published_year: Optional[int] = None
    isbn: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True 