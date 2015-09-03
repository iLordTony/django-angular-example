# Create your views here.
from django.views.generic import TemplateView
from rest_framework import generics

from api.serializers import UserSerializer, PostSerializer, PhotoSerializer
from api.models import User, Post, Photo

# Todas las vistas del API


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')

        return Post.objects.filter(author__username=username)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostPhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(post__pk=self.kwargs.get('pk'))


class PhotoList(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        print self.kwargs.get('template_name')
        return [self.kwargs.get('template_name') + ".html"]
