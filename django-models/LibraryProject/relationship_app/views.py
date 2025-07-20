from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic.detail import DetailView

def home(request):
    return HttpResponse("<h1>Welcome to the Library App</h1><p><a href='/books/'>View Books</a></p>")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

# Create your views here.
# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
