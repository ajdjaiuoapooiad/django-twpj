from django.shortcuts import render

from core.models import Post


def index(request):
    posts = Post.objects.filter(active=True,visibility='Everyone')
    context = {
        'posts': posts,
    }
    return render(request,'index.html',context)

def detail(request,slug):
    post = Post.objects.get(active=True,visibility='Everyone',slug=slug)
    context = {
        'p': post,
    }
    return render(request,'detail.html',context)
