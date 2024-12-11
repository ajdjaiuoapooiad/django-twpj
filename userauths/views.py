from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render

from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
User=settings.AUTH_USER_MODEL


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form=UserRegisterForm(request.POST or None)
        
        try:
            if form.is_valid():
                user=form.save()
                login(request,user)
                return redirect('index')
        except:
            messages.error(request,f'An error has occurred')
    else:
        form=UserRegisterForm()
        
    context={
        'form': form,
    }
    
    return render(request,'register.html',context)