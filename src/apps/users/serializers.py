from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserBase = get_user_model()



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                raise serializers.ValidationError("Incorrect: username or password")

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ('id', 'username', 'is_active')