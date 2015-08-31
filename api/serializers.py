from api.models import User, Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedIdentityField(view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id','email', 'first_name', 'last_name', 'username', 'post')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    class Meta:
        model = Post