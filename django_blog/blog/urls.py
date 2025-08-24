from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import (
    CommentCreateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", views.profile_view, name="profile"),

    path("posts/", PostListView.as_view(), name="post-list"),
   
    
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),


    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path("posts/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add_comment"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit_comment"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete_comment"),
]

