from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

def home(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all(),
    return render(request, 'index.html', {'posts': all_posts})