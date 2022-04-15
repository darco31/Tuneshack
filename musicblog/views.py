from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.


class HomeView(ListView):

    model = Post
    template_name = 'home.html'


class PostView(DeleteView):

    model = Post
    template_name = 'post_detail.html'


class AddPost(CreateView):

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'