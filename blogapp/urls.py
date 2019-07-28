from django.urls import path, include
from . import views
from django.contrib import admin
import blogapp.urls
import blogapp.views


urlpatterns = [
    path('blogapp/<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('blogapp/create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('addcomment/<int:pk>', views.addcomment, name='addcomment'),
    
]