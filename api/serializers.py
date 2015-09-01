from api.models import User, Post, Photo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'posts')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    photos = serializers.HyperlinkedIdentityField(view_name='postphoto-list')

    class Meta:
        model = Post
        fields = ('author', 'photos', 'id', 'title', 'body',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo