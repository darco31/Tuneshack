from django.urls import path
from .views import HomeView, PostView, AddPost

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('posts/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]
