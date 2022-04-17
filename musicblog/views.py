from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):

    model = Post
    template_name = 'home.html'
    ordering = ['-id']


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
    """
    Use reverse lazy below to redirect user to
    home page on deletion of post
    https://docs.djangoproject.com/en/4.0/ref/urlresolvers/
    """

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')