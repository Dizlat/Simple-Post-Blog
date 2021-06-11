from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    n = ['Dizlat', 'Ur']
    return render(request, 'blog/index.html', {'names': n})
