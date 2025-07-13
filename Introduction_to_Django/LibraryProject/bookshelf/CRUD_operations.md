# CRUD Operations on Book Model

## Create

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output:
# <Book: 1984 by George Orwell (1949)>

# Retrieve
# Retrieve Book


# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

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
# Delete Book and Confirm Deletion


from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)

# Output:
# <QuerySet []>
