from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogpost(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})


def blogdetail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'details': details})
