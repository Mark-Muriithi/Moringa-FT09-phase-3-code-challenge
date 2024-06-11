class Article:
    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def author(self):
        return self.author

    def magazine(self):
        return self.magazine
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Author(Base):
    _tablename_ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Magazine(Base):
    _tablename_ = 'magazines'
    _init_()
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)

class Article(Base):
    _tablename_ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))
    author = relationship('Author', backref='articles')
    magazine = relationship('Magazine', backref='articles')

engine = create_engine('sqlite:///database.db')