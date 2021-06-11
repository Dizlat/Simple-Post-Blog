from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts-list'),
    path('post/<str:slug>/', post_detail, name='post-detail'),
]