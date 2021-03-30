from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('dradmin/', admin.site.urls),
    #path('course/', include('courseAPI.urls'),name="course"),
    #path('movies/', include('movieAPI.urls'),name="movies"),
    # path('login/', include('loginview.urls')),
]