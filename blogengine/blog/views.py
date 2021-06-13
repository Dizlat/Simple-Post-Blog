from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', locals())

class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', locals())


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', locals())

class TagDetail(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', locals())