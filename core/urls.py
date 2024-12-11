from django.contrib import admin
from django.urls import include, path

from core import views


urlpatterns = [
    path('',views.index, name='index'),
    path('post/<str:id>/',views.detail, name='detail'),
    path('post-create/',views.create_post, name='create-post'),
    path('delete/<str:id>/',views.delete_post, name='delete-post'),
]