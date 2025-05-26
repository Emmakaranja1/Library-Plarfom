# Library Platform

A modern library management system built with SQLAlchemy and Typer CLI that allows tracking of books, categories, and members.

## Features

- Command-line interface for easy management
- Book management (list, add, update, delete)
- Category and Member management
- Database integration with SQLAlchemy ORM
- Clean architecture with controllers and models

## Technologies Used

- Python 3.10
- SQLAlchemy (ORM for database operations)
- Typer (CLI interface)
- PostgreSQL database
- psycopg2 (PostgreSQL adapter for Python)
- python-dotenv (for environment variable management)

## Setup and Installation

### Prerequisites

- Python 3.10 or higher
- PostgreSQL database
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
2. Set up a virtual environment:
3. Activate the virtual environment:

- On macOS/Linux:
  ```
  source env/bin/activate
  ```
- On Windows:
  ```
  env\Scripts\activate
  ```

4. Install dependencies:

```
 pip install -r requirements.txt
```

5. Create a `.env` file in the project root with your PostgreSQL connection details:

```
PGHOST=localhost
PGPORT=5432
PGDATABASE=library_db
PGUSER=your_username 
PGPASSWORD=your_password
```

6. Configure your database connection:
   - Create a `.env` file in the project root with your PostgreSQL connection details
   - The database schema is managed through SQLAlchemy models

## Running the Application

The application uses Typer for its CLI interface. Here are the available commands:

```bash
# View help information and available commands
python main.py --help

# List all books in the library
python main.py list-books

# Test the CLI
python main.py hello "Your Name"
```

### Commands

| Command | Description |
|---------|-------------|
| `list-books` | Display all books in the library |
| `hello [NAME]` | Simple greeting command (example) |

## Project Structure

```
library-platform/
├── controllers/
│   └── books.py         # Book-related controller methods
├── db/
│   ├── config.py        # Database configuration
│   └── database.py      # SQLAlchemy database setup
├── models/
│   ├── book.py          # Book model
│   ├── category.py      # Category model
│   └── member.py        # Member model
├── main.py              # CLI entry point with Typer commands
├── requirements.txt     # Project dependencies
└── README.md
```

## Database Models

The application uses SQLAlchemy ORM with the following models:

- **Book**: Represents books in the library with title, ISBN, publication date, and copy information
- **Category**: Categorizes books (fiction, non-fiction, etc.)
- **Member**: Library members who can borrow books

## License

The README includes:
1. Project overview
2. Features
3. Technologies used
4. Setup and installation instructions
5. Running instructions
6. Project structure overview
7. License information

You may want to add more specific details about functionality as you develop the application further.