from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    posts = Posts.objects.order_by()[::]
    context = {
            'title' : 'Посты',
            'posts' : posts
        }
    return render(request, 'posts/index.html', context)

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/detail_view.html'
    context_object_name = 'post'
    
    

class PostUpdateView(UpdateView):
    model = Posts
    template_name = "posts/create.html"
    form_class = PostsForm
    


class PostsDeleteView(DeleteView):
    model = Posts
    success_url = '/posts/'
    template_name = "posts/delete.html"    


class CreatePost(CreateView):
    model = Posts
    success_url = '/posts/'
    template_name = "posts/create.html"
    form_class = PostsForm

