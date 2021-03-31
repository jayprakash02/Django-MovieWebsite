from rest_framework import serializers
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField( max_length=50,blank=True,null=True)
    image = models.ImageField( upload_to='Person', height_field=None, width_field=None, max_length=None,blank=True,null=True)


class Movie(models.Model):
    name = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='banner',blank=True)
    banner = models.ImageField(upload_to='banner',blank=True)
    url = models.URLField(blank=True)
    small_description = models.CharField( max_length=50,blank=True,null=True)
    story_description = models.CharField( max_length=500,blank=True,null=True)
    date_created = models.DateTimeField( auto_now_add=True)
    movie_release_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    featured = models.BooleanField(default=False)
    length = models.TimeField(auto_now=False, auto_now_add=False)
    directors = models.ManyToManyField("Person",related_name='director')
    stars = models.ManyToManyField("Person",related_name='star')
    writter = models.ManyToManyField("Person",related_name='writter')

    class Meta:
        ordering = ['-date_created']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'