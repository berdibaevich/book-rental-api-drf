from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, response

from .serializers import (
    SignUpSerializer,
    MeSerializer,
    UserTokenObtainPairSerializer
)



@api_view(['POST'])
def tokenObtainPairView(request):
    serializer = UserTokenObtainPairSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK)



@api_view(['POST'])
def signup_api(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    refresh = UserTokenObtainPairSerializer.get_token(user)

    return response.Response(
        {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        },
        status=status.HTTP_201_CREATED
    )



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_api(request):
    serializer = MeSerializer(request.user)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)