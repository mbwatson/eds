from django.shortcuts import get_object_or_404, render

def index(request):
    context = {
        'page_title': 'Blog',
    }
    return render(request, 'blog/index.html', context)

