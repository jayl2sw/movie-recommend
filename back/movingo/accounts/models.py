from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=16)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    

    def __str__(self):
        return self.username