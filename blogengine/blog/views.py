from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', locals())


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', locals())