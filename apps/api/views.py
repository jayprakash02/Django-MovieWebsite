from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from .models import *
# Create your views here.

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
