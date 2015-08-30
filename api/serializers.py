from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Post, Photo

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False) #hacemos esto para que pueda leer el campo author
    photos = PhotoSerializer(required=False)

    class Meta:
        model = Post
        fields = ('title','author', 'body', 'photos',)




