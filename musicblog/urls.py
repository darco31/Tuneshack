from django.urls import path
from .views import (
    HomeView, PostView, AddPost, EditPost, DeletePost,
    LikesPost, AddComment
)
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
    path('posts/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('posts/edit_post/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('blogpost-like/<int:pk>', views.LikesPost, name="blogpost_like"),
    path
    ('article/<int:pk>/add_comment', AddComment.as_view(), name='add_comment'),
]

HANDLER400 = 'musicblog.views.handler400'
HANDLER400 = 'musicblog.views.handler403'
HANDLER400 = 'musicblog.views.handler404'
HANDLER400 = 'musicblog.views.handler500'
