from rest_framework import serializers 
from .models import MyUser
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password']