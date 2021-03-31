from rest_framework import serializers
from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='banner',blank=True)
    url = models.URLField(blank=True)


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'