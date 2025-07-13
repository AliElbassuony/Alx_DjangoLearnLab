# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)

# Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
