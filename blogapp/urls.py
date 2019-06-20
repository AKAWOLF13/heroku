from django.urls import path
from . import views

urlpatterns = [
    path('blogapp/<int:blog_id>/', views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('blogapp/create/', views.create, name='create'),
]