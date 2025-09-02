from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
