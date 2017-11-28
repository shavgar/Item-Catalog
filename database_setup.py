import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


# class to store user info
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    image = Column(String(250))
    provider = Column(String(25))


# class for Books Database
class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    Book_Title = Column(String(250), nullable=False)
    Author = Column(String(250), nullable=False)
    URL = Column(String(450), nullable=False)
    description = Column(String(), nullable=False)
    category = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # return book data in serializable format
        return {
            'id': self.id,
            'name': self.Book_Title,
            'author': self.Author,
            'genre': self.category,
            'URL': self.URL,
            'Book_description': self.Book_description
        }

engine = create_engine('sqlite:///BookCatalog.db')
Base.metadata.create_all(engine)