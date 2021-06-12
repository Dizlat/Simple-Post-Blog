from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts-list'),
    path('post/<str:slug>/', post_detail, name='post-detail'),
    path('tags/', tags_list, name='tags-list'),
    path('tag/<str:slug>/', tag_detail, name='tag-detail'),
]