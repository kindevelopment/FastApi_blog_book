from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base

from auth.models import User

metadata = MetaData()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(5000))
    user_id = Column(Integer, ForeignKey('user.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    date_publication = Column(TIMESTAMP, default=datetime.utcnow)
    file = Column(String(5000), nullable=False)
    date_created_post = Column(TIMESTAMP, default=datetime.utcnow)
    num_pages = Column(Integer, nullable=False)
    permit = Column(Boolean, default=False, nullable=False)
    user = relationship('User', backref='books')
    category = relationship('Category', backref='books')
    publisher = relationship('Publisher', backref='books')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)


book_author = Table(
    'book_author',
    metadata,
    Column('book', ForeignKey(Book.id)),
    Column('author', ForeignKey(Author.id)),
)


book_genre = Table(
    'book_genre',
    metadata,
    Column('book', ForeignKey(Book.id)),
    Column('genre', ForeignKey(Genre.id)),
)


likes = Table(
    'likes',
    metadata,
    Column('book', ForeignKey(Book.id)),
    Column('user', ForeignKey(User.id)),
)


dislikes = Table(
    'dislikes',
    metadata,
    Column('book', ForeignKey(Book.id)),
    Column('user', ForeignKey(User.id)),
)