from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms import PostForm
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

def delete_post(request,slug):
    post = Post.objects.get(active=True,visibility='Everyone',slug=slug)
    post.delete()
    return redirect('index')

def create_post(request):
    if request.method == 'POST':
        form=PostForm(request.POST or None)
        
        try:
            if form.is_valid():
                post=form.save()
                return redirect('index')
        except:
            messages.error(request,f'An error has occurred')
    else:
        form= PostForm()
        
    context = {
        'form': form,
    }
    return render(request,'post_create.html',context)