from fastapi import APIRouter, Depends
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Book, Category, Genre, Author, Publisher
from .schema import AddBook, AddCategory
from database import get_async_session

router_blog = APIRouter(
    prefix="/book",
    tags=["Books"]
)


@router_blog.post('/add_book')
async def add_book(new_book: AddBook, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(book).values(**new_book.dict())
    await session.execute(stmt)
    await session.commit()
    return {'data': new_book}


@router_blog.post('/add_category')
async def add_category(new_category: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(category).values(**new_category.dict())
    await session.execute(stmt)
    await session.commit()
    return {'data': new_category}



@router_blog.post('/add_genre')
async def add_genre(new_genre: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(genre).values(**new_genre.dict())
    await session.execute(stmt)
    await session.commit()
    return {'data': new_genre}


@router_blog.post('/add_author')
async def add_author(new_author: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(author).values(**new_author.dict())
    await session.execute(stmt)
    await session.commit()
    return {'data': new_author}


@router_blog.post('/add_publisher')
async def add_publisher(new_publisher: AddCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(publisher).values(**new_publisher.dict())
    await session.execute(stmt)
    await session.commit()
    return {'data': new_publisher}


# @router_blog.get('/get_book')
# async def get_book(book: GetBook)