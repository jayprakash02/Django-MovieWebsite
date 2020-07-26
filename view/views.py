from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post, Comment
# Create your views here.


def index(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    return render(request, 'corona.html',{'post':post,'comment':comment})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
