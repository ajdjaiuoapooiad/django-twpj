from django.contrib import admin
from django.urls import include, path

from core import views


urlpatterns = [
    path('',views.index, name='index'),
    path('post/<slug:slug>/',views.detail, name='detail'),
    path('',views.index, name='index'),
    path('',views.index, name='index'),
]