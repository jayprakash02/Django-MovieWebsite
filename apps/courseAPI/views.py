from django.shortcuts import render

# Create your views here.
from .models import CourseAPI
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CourseAPI.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]