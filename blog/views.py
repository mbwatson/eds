from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Category, Post

def index(request):
    posts = get_list_or_404(Post)
    context = {
        'page_title': 'Blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    context = {
        'page_title': 'Blog Post',
    }
    return render(request, 'blog/detail.html', context)
