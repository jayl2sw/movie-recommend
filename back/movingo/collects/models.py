from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Hashtag(models.Model):
    tag = models.CharField(max_length=20)

class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie, blank=True, related_name='collections')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_collections', blank=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='movies', blank=True)
    on_main = models.BooleanField(default=False)

