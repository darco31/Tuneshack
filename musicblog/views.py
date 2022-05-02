from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment
from .forms import PostForm, EditForm, AddComment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


class HomeView(ListView):

    model = Post
    template_name = "home.html"
    ordering = ["-created_on"]
    paginate_by = 3


def contact(request):
    return render(request, "contact.html", {})


def thanks(request):
    return render(request, "thanks.html", {})


class PostView(DetailView):

    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs["pk"])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data["number_of_likes"] = likes_connected.number_of_likes()
        data["post_is_liked"] = liked
        return data


def LikesPost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("blogpost_id"))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))


class AddPost(CreateView):

    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class AddComment(CreateView):

    model = Comment
    form_class = AddComment
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    success_url = reverse_lazy("home")


class EditPost(UpdateView):

    model = Post
    form_class = EditForm
    template_name = "edit_post.html"


class DeletePost(DeleteView):
    """
    Use reverse lazy below to redirect user to
    home page on deletion of post
    https://docs.djangoproject.com/en/4.0/ref/urlresolvers/
    """

    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


def handler400(request, exception):
    return render(request, "400.html", status=400)


def handler403(request, exception):
    return render(request, "403.html", status=403)


def handler404(request, exception):
    return render(request, "404.html", status=404)


def handler500(request, exception):
    return render(request, "500.html", status=500)
