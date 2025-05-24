from rest_framework import serializers 
from .models import MyUser

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        groups = validated_data.pop('groups', None)  # Remove M2M field if present

        # Extract image from validated_data if present
        image = validated_data.pop('image', None)  

        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),
            gender=validated_data.get('gender', ''),
            dob=validated_data.get('dob', None),
            address=validated_data.get('address', ''),
            # assign image here if present
            image=image,
        )
        user.set_password(validated_data['password'])
        user.save()

        if groups:
            user.groups.set(groups)

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Handle image if it exists in update data
        image = validated_data.pop('image', None)
        if image is not None:
            instance.image = image

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
