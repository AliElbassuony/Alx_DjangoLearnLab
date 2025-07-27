# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Output:
# Nineteen Eighty-Four
