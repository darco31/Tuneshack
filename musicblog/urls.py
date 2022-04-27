from django.urls import path
from .views import (
    HomeView, PostView, AddPost, EditPost, DeletePost,
    LikesPost, AddComment
)
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('posts/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('posts/edit_post/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('blogpost-like/<int:pk>', views.LikesPost, name="blogpost_like"),
    path
    ('article/<int:pk>/add_comment', AddComment.as_view(), name='add_comment'),
]
