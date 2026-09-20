from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

UserBase = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=5)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = UserBase
        fields = ('id', 'username', 'password', 'token')

    def create(self, validated_data):
        user = UserBase.objects.create(
            username = validated_data.get('username'),
            password = validated_data.get('password')
        )

        token = Token.objects.create(user = user)
        user.token = token
        return user

    


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