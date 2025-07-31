from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    genres = models.TextField(null=True)
    languages=models.TextField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

