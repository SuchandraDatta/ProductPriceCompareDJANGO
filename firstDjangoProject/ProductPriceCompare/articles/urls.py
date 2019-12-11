from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('submitted/', views.submitted, name='submitted'),
    path('', views.article_list, name='article_list'),
]