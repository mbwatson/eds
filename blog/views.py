from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Post

def PostListView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context

def PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

def index(request):
    template = 'blog/index.html'
    objects_list = Post.objects.all()

    context = {
        'posts': objects_list,
    }
    return render(request, template, context)

def detail(request, post_slug):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post': post,
    }
    return render(request, template, context)

# def index(request):
#     posts = get_list_or_404(Post)
#     context = {
#         'page_title': 'Blog',
#         'posts': posts,
#     }
#     return render(request, 'blog/index.html', context)

# def detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {
#         'page_title': 'Blog Post',
#         'post': post,
#     }
#     return render(request, 'blog/detail.html', context)
