# Library Management System API

A FastAPI-based Library Management System that provides CRUD operations for managing books.

## Features

- Create, Read, Update, and Delete books
- SQLite database with SQLAlchemy ORM
- Pydantic models for request/response validation
- Swagger UI documentation
- Error handling for common scenarios

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

- `POST /books/`: Create a new book
- `GET /books/`: Get all books
- `GET /books/{book_id}`: Get a specific book by ID
- `PUT /books/{book_id}`: Update a book
- `DELETE /books/{book_id}`: Delete a book

## Example Usage

### Create a Book
```bash
curl -X POST "http://localhost:8000/books/" -H "Content-Type: application/json" -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "978-0743273565"
}'
```

### Get All Books
```bash
curl "http://localhost:8000/books/"
```

### Get a Specific Book
```bash
curl "http://localhost:8000/books/1"
```

### Update a Book
```bash
curl -X PUT "http://localhost:8000/books/1" -H "Content-Type: application/json" -d '{
    "title": "Updated Title"
}'
```

### Delete a Book
```bash
curl -X DELETE "http://localhost:8000/books/1"
``` 