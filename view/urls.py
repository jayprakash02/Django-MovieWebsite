from django.contrib import admin
from django.urls import path ,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', views.index , name='main'),
    path('',include(router.urls) ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

