from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

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


class EditPost(UpdateView):

    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    # fields = ['title', 'body']


class DeletePost(DeleteView):

    model = Post
    template_name = 'delete_post.html'