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
