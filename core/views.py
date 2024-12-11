from django.shortcuts import render

from core.models import Post


def index(request):
    posts = Post.objects.filter(active=True,visibility='Everyone')
    context = {
        'posts': posts,
    }
    return render(request,'index.html',context)
