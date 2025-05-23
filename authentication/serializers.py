from rest_framework import serializers 
from .models import MyUser

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # ensures password isn't returned in API response
        }

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # hashes the password
        user.save()
        return user
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value) #for updating the other attributes

        if password:
            instance.set_password(password)  # hashes the password
        instance.save()
        return instance
