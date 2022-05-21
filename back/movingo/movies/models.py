from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.TextField()
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    vote_average = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    popularity = models.FloatField(default=0)
    adult = models.BooleanField(default=False)
    view_cnt = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    related_movies = models.ManyToManyField("self", blank=True)
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    RATE_CHOICE = (
		(5.0, 5),
        (4.5, 4.5),
        (4.0, 4),
        (3.5, 3.5),
        (3.0, 3),
        (2.5, 2.5),
        (2.0, 2),
        (1.5, 1.5),
        (1.0, 1),
    )
    rate = models.FloatField(choices= RATE_CHOICE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return self.created_at.date

    def __str__(self):
        return self.content