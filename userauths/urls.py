
from django.urls import path

from userauths import views


urlpatterns = [
    path('register/',views.register,name='register'),
    
]

