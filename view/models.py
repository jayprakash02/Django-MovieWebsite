from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    pubdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    shortdesc = models.CharField(max_length=100)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)