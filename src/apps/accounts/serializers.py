from rest_framework import serializers
from django.contrib.auth import get_user_model

UserBase = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=5)

    class Meta:
        model = UserBase
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = UserBase.objects.create_user(
            username = validated_data.get('username'),
            password = validated_data.get('password')
        )
        return user

    


class MeSerializer(serializers.ModelSerializer):
    """Profile me"""
    class Meta:
        model = UserBase
        fields = ('id', 'username', 'is_active')