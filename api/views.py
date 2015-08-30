from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from api.models import Post, Photo
from api.serializers import PostSerializer, PhotoSerializer,UserSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer