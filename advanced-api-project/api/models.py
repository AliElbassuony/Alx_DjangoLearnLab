from django.db import models
from django.utils import timezone

from django.db import models


# Author model — stores details about a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name


# Book model — stores details about books written by an Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',  # Enables reverse access: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
