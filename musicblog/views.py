from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):

    model = Post
    template_name = 'home.html'


class PostView(DeleteView):

    model = Post
    template_name = 'post_detail.html'


class AddPost(CreateView):

    model = Post
    template_name = 'add_post.html'
    fields = '__all__'