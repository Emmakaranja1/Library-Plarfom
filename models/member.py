from datetime import date
from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, func 
from db.database import Base

@dataclass
class Member:
    id: Optional[int]
    first_name: str
    last_name: str
    surname: str
    email: str
    joined_date: Optional[date]

class MemberModel(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    joined_date = Column(Date, nullable=False, default=func.now())

    def __init__(self, first_name, last_name, surname, email):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return f"<Member(first_name={self.first_name}, last_name={self.last_name}, surname={self.surname}, email={self.email})>"
    
    def create(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
        print(f"{self.first_name} {self.last_name} member has been added successfully!!")
        return self
    
    def update(self, session):
        session.commit()
        session.refresh(self)
        print(f"{self.first_name} {self.last_name} member has been updated successfully!!")
        return self
    
    def delete(self, session):
        session.delete(self)
        session.commit()
        print(f"{self.first_name} {self.last_name} member has been deleted successfully!!")
        return True