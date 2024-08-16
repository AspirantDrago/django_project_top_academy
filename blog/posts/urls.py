from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('create', CreatePost.as_view(), name='create'),
    path('<int:pk>/', PostsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', PostsDeleteView.as_view(), name='delete'),
]