# API Endpoints for Books

## Public Endpoints
- **GET** `/api/books/` → List all books
- **GET** `/api/books/<id>/` → Retrieve a single book

## Authenticated Endpoints
- **POST** `/api/books/create/` → Create a new book
- **PUT/PATCH** `/api/books/<id>/update/` → Update an existing book
- **DELETE** `/api/books/<id>/delete/` → Delete a book

## Permissions
- Public: Read operations
- Authenticated: Write operations
- Validation: Publication year cannot be in the future.
