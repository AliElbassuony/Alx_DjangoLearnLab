from django.db import models

# Create your models here.

# Author Model with string field name
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# Book Model with 3 field (string name, integer publication_year,foreignkey author)
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField() 
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables reverse access: author.books.all()
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return f"{self.title} ({self.publication_year})"