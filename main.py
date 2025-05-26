import typer

# DB IMPORTS 
from db.database import get_db, SessionLocal
from controllers import books

app = typer.Typer(help="📚 Manage your books via CLI")

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command(help="List all books in the library")
def list_books():
    """
    List all books in the library.
    """
    with SessionLocal() as session:
        all_books = books.list_books(session)
        if all_books:
            for book in all_books:
                typer.echo(
                    f"Title: {book.title}, ISBN: {book.isbn}, Published Date: {book.published_date}, Total Copies: {book.total_copies}, Available Copies: {book.available_copies}")
        else:
            typer.echo("🚫 No books found.")


if __name__ == "__main__":
    app()
