# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, home
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    
    path('', home, name='home'),  # ✅ Root path
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]
