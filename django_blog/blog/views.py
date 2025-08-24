from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegisterForm
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm
from django.db.models import Q

# Create your views here.
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["pk"]})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def get_queryset(self):
        # Only the author can edit their own comments
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"

    def get_queryset(self):
        # Only the author can delete their own comments
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.id})
    

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 5  # optional pagination

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})



def search_posts(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, "blog/search_results.html", {"query": query, "results": results})


def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__iexact=tag_name)
    return render(request, "blog/posts_by_tag.html", {"tag": tag_name, "posts": posts})