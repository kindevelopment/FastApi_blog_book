import datetime

from pydantic import BaseModel, Field


class AddBook(BaseModel):
    title: str
    description: str
    user: int
    category: int
    publisher: int
    date_publication: datetime.datetime
    date_created_post: datetime.datetime
    num_pages: int
    permit: bool = False


class AddCategory(BaseModel):
    title: str


class AddGenre(BaseModel):
    title: str


class AddAuthor(BaseModel):
    title: str


class AddPublisher(BaseModel):
    title: str


class GetBook(BaseModel):
    id: int
    title: str