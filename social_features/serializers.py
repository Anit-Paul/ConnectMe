from .models import Follow,Post
from rest_framework import serializers

class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'