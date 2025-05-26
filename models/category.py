from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, func 
from db.database import Base


@dataclass
class Category:
    id: Optional[int]
    title: str
    description: Optional[str] = None


class CategoryModel(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(500), nullable=True)

    def __init__(self, title: str, description: Optional[str] = None):
        self.title = title
        self.description = description

    def __repr__(self):
        return f"<Category(title={self.title}, description={self.description})>"
    
    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"{self.title} category has been added successfully!!")
        return self
    
    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"{self.title} category has been updated successfully!!")
        return self
    
    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"{self.title} category has been deleted successfully!!")
        return True
    
