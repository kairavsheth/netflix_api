from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('subscriber', 'Subscriber'),
    )
    role = models.CharField(max_length=10, choices=ROLES)


class Video(models.Model):
    GENRES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=10, choices=GENRES)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
