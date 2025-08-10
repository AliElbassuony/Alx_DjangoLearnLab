from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints:
    - CRUD operations
    - Filtering, Searching, Ordering
    - Permissions
    """

    def setUp(self):
        """
        Setup test data for all test methods.
        """
        # Create a user for authenticated actions
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="Aldous Huxley")

        # Create books
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author1
        )
        self.book3 = Book.objects.create(
            title="Brave New World", publication_year=1932, author=self.author2
        )

        # API URLs
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

# ---------- CRUD Tests ----------

    def test_list_books(self):
        """Test retrieving all books (public)"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID (public)"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_requires_authentication(self):
        """Test creating a book without authentication fails"""
        data = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication succeeds"""
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication succeeds"""
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "Updated Title",
            "publication_year": 1950,
            "author": self.author1.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication succeeds"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
# ---------- Filter, Search, Order Tests ----------

    def test_filter_books_by_author(self):
        """Test filtering books by author name"""
        response = self.client.get(f"{self.list_url}?author__name=George Orwell")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        """Test searching books by keyword"""
        response = self.client.get(f"{self.list_url}?search=Brave")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Brave New World")

    def test_order_books_by_year(self):
        """Test ordering books by publication_year"""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
