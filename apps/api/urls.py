from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('',index_view),
    path('api/', include(router.urls)),
]