import datetime

from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Book, Category, Genre, Author, Publisher
from .schema import AddBook, AddCategory
from database import get_async_session

from .service import save_photo

router_blog = APIRouter(
    prefix="/book",
    tags=["Books"]
)


@router_blog.post('/add_book')
async def add_book(
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        user: int = Form(...),
        date_publication: datetime.datetime = Form(default=datetime.datetime.utcnow()),
        date_created_post: datetime.datetime = Form(default=datetime.datetime.utcnow()),
        category: int = Form(...),
        genre: int = Form(...),
        publisher: int = Form(...),
        num_pages: int = Form(...),
        session: AsyncSession = Depends(get_async_session)
):
    result = await save_photo(title, file)
    data = AddBook(
        title=title,
        description=description,
        file=result,
        user_id=user,
        date_publication=date_publication,
        date_created_post=date_created_post,
        category_id=category,
        publisher_id=publisher,
        genre=genre,
        num_pages=num_pages,
        permit=False
    )
    instance = Book(**data.dict())
    session.add(instance)
    await session.commit()
    return {'data': 'successs'}


@router_blog.post('/add_category')
async def add_category(new_category: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = Category(**new_category.dict())
    session.add(stmt)
    await session.commit()
    return {'data': new_category}


@router_blog.post('/add_genre')
async def add_genre(new_genre: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = Genre(**new_genre.dict())
    session.add(stmt)
    await session.commit()
    return {'data': new_genre}


@router_blog.post('/add_author')
async def add_author(new_author: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = Author(**new_author.dict())
    session.add(stmt)
    await session.commit()
    return {'data': new_author}


@router_blog.post('/add_publisher')
async def add_publisher(new_publisher: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = Publisher(**new_publisher.dict())
    session.add(stmt)
    await session.commit()
    return {'data': new_publisher}


