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


## Filtering
Filter by year:
GET /api/books/?publication_year=1945

Filter by author name:
GET /api/books/?author__name=George%20Orwell

## Searching
Search for keyword in title or author:
GET /api/books/?search=Farm

## Ordering
Order by year ascending:
GET /api/books/?ordering=publication_year

Order by year descending:
GET /api/books/?ordering=-publication_year