from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    imdb = models.FloatField(blank=True)
    link = models.URLField()
    imageLink = models.URLField()
    ssLink = models.URLField(blank=True)

    def __str__(self):
        return self.name