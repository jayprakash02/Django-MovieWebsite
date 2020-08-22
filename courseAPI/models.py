from django.db import models

# Create your models here.
class CourseAPI(models.Model):
    courseid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    url = models.URLField()