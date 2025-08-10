from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# List all books (public)
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books in the system.
    Public access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    # Search fields (partial matches)
    search_fields = ['title', 'author__name']
     # Enable filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# Retrieve a single book (public)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Returns a single book by ID.
    Public access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book entry.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/update/
    Updates a book entry.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Deletes a book entry.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

