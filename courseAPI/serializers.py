from .models import CourseAPI
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseAPI
        fields ='__all__'