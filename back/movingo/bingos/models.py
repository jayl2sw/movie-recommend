from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Bingo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, related_name='bingos')
