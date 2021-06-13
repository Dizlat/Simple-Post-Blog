from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from .forms import TagForm
from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', locals())


class TagDetail(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(Tag.get_absolute_url())
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', locals())