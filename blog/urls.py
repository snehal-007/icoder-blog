from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    #API to post comments
    path('postComment' , views.postComment, name='postComment'),
    
    path('', views.bloghome, name='BlogHome'),
    path('<str:slug>/', views.blogpost, name='BlogPost'),


]
