from .models import Follow
from rest_framework import serializers

class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'