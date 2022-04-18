from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Post model outlined below


class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    """
    Below function redirects when user submits a new post
    """
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
