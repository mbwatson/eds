from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Post

def index(request):
    posts = get_list_or_404(Post)
    published_posts = filter(lambda p: p.published(), posts)

    context = {
        'page_title': 'Blog',
        'posts': published_posts,
    }
    return render(request, 'blog/index.html', context)

def detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'page_title': post.title,
        'post': post,
    }
    return render(request, 'blog/detail.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post, category=category.pk)
    context = {
        'page_title': category.title,
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)
