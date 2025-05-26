from datetime import date
from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, func 
from db.database import Base


@dataclass
class Book:
    id: Optional[int]
    title: str
    isbn: Optional[str]
    published_date: Optional[date]
    total_copies: int
    available_copies: int
    category_id: Optional[int] = None


class BookModel(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    isbn = Column(String(13), nullable=False, unique=True)
    published_date = Column(Date, nullable=False, default=func.now())
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)
    # category_id = 

    def __init__(self, title, isbn, published_date, total_copies, available_copies):
        self.title = title
        self.isbn = isbn
        self.published_date = published_date
        self.total_copies = total_copies
        self.available_copies = available_copies

    def __repr__(self):
        return f"<Book(title={self.title}, isbn={self.isbn}, published_date={self.published_date}, total_copies={self.total_copies}, available_copies={self.available_copies})>"
    

    # create crud operations methods here if needed 

    def create(self: Book, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"{self.title} book has been added successfully!!")
        return self
    
    def update(self: Book, session):
        session.commit()
        session.refresh(self)
        print(f"{self.title} book has been updated successfully!!")
        return self
    
    def delete(self: Book, session):
        session.delete(self)
        session.commit()
        print(f"{self.title} book has been deleted successfully!!")
        return True

    


