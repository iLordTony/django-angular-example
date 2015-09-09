# Create your views here.
from django.views.generic import TemplateView
from rest_framework import generics

from api.serializers import UserSerializer, PostSerializer, PhotoSerializer
from api.models import User, Post, Photo

from api.permissions import PostAuthorCanEditPermission

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


class PostMixin(object):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostAuthorCanEditPermission, ]

    def pre_save(self, obj):
        print 'Algo'
        obj.author = self.request.user
        return super(PostMixin, self).pre_save(obj)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


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


"""Aqui terminan las vistas del API, estas son todas las vista en web"""


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


# Rendereamos deacuerdo a la url que a la que se le da click
class SimpleStaticView(TemplateView):
    # Lo usamos en lugar de un template_name
    def get_template_names(self):
        print self.kwargs.get('template_name')
        return [self.kwargs.get('template_name') + ".html"]
