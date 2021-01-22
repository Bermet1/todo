from django.db import models

# Create your models here.

class todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)
    description = models.TextField(max_length=600)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.DateField()
    date = models.DateField(auto_now_add=True)