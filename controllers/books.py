from sqlalchemy.orm import Session 
from models.book import BookModel, Book
from db.database import get_db


# dependency injection to get the database session -> Session -> Models -> DB - return data as objects

# list all books
def list_books(session: Session = get_db()): 
    books = session.query(BookModel).all()
    return books

    #LIST COMREHENSION ??? HOW CAN IT BE USED 
    # return [Book(**book.__dict__) for book in books]  # Convert SQLAlchemy model instances to Book dataclass instances


# get one book 
def get_book(book_id: int, session: Session = get_db()): 
    book = session.query(BookModel).filter(BookModel.id == book_id).first()
    if book: 
        return Book(**book.__dict__)
    return None

# create a book
def create_book(book_data: Book, session = get_db()): 
    new_book = BookModel(
        title=book_data.title,
        isbn=book_data.isbn,
        published_date=book_data.published_date,
        total_copies=book_data.total_copies,
        available_copies=book_data.available_copies
    )
    result = BookModel.create(new_book, session)
    return result  # Return the created book instance

# update a book 
def update_book(book_id, book_data, session = get_db()):
    # check if there book exists 
    book = session.query(BookModel).filter(BookModel.id == book_id).first()

    # perform an update operation 
    if book: 
        book.title = book_data.title
        book.isbn = book_data.isbn
        book.published_date = book_data.published_date
        book.total_copies = book_data.total_copies
        book.available_copies = book_data.available_copies
        return BookModel.update(book, session)
    return None  # Return None if the book does not exist

# delete a book
def delete_book(book_id, session = get_db()):
    book = session.query(BookModel).filter(BookModel.id == book_id).first()
    if book:
        return BookModel.delete(book, session)
    return None  # Return None if the book does not exist