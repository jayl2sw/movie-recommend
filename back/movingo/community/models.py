from django.db import models
from movies.models import Movie

# Create your models here.
class Thread(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __self__(self):
        return self.movie
    
class Comments(models.Model):
    thread = models.ForeignKey(Thread, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.content