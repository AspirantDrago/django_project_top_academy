from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='posts'),
    path('create', create, name='posts_create'),
    path('<int:pk>/', PostsDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostsDeleteView.as_view(), name='post_delete'),
    
    
]