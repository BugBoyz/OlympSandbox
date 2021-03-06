from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=25)
    date = models.DateField()
    tags = models.CharField(max_length=30)
