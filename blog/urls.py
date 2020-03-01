from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.bloghome, name='BlogHome'),
    path('<str:slug>/', views.blogpost, name='BlogPost'),

]
