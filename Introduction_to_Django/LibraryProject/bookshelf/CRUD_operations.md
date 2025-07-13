# CRUD Operations on Book Model

## Create

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output:
# <Book: 1984 by George Orwell (1949)>

# Retrieve
# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Output:
# 1984 George Orwell 1949

# Update
# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Output:
# Nineteen Eighty-Four

# Delete
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)

# Output:
# <QuerySet []>
