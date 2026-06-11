# 📘 Assignment: Build a REST API with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice API design, request validation, and CRUD-style routing.

## 📝 Tasks

### 🛠️ Create the API Service

#### Description
Create a FastAPI application that exposes endpoints for managing a small collection of books.

#### Requirements
Completed project should:

- Use FastAPI to define the API service.
- Include a simple in-memory data store (a list or dictionary) for storing book records.
- Support the following endpoints:
  - `GET /books` — return a list of all books.
  - `GET /books/{book_id}` — return a single book by ID.
  - `POST /books` — add a new book.
  - `PUT /books/{book_id}` — update an existing book.
  - `DELETE /books/{book_id}` — remove a book.
- Use Pydantic models for request and response validation.
- Return appropriate HTTP status codes for success and error conditions.

### 🛠️ Add Validation and Error Handling

#### Description
Add request validation and clear error responses for invalid or missing data.

#### Requirements
Completed project should:

- Validate request bodies using Pydantic models.
- Ensure required fields include `title`, `author`, and `year`.
- Return `404 Not Found` if a book ID is not found.
- Return `400 Bad Request` for invalid input.
- Include descriptive error messages for invalid requests.

## 🚀 How to run

Install FastAPI and Uvicorn if needed:

```bash
pip install fastapi uvicorn
```

Run the API server from the assignment folder:

```bash
uvicorn starter_code:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the API.

## 📂 Files

- `starter_code.py` — starter FastAPI app and example book data.

## ✅ Submission

- Submit the completed `starter_code.py` with your FastAPI implementation.
- Ensure the API runs without errors and supports all required routes.
- Include comments describing your models and route handlers.

## ✨ Extensions (optional)

- Add query parameters for filtering books by author or year.
- Add pagination to `GET /books`.
- Add a `rating` field and allow sorting results by rating.

## 🎓 Learning Outcomes

- Build and run a FastAPI application.
- Design RESTful routes and use HTTP methods correctly.
- Validate input with Pydantic and handle API errors cleanly.
- Practice using Python data structures to store and update resources.
