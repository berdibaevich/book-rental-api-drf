from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    SignUpSerializer,
    MeSerializer
)


@api_view(['POST'])
def signup_api(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username
    refresh['role'] = user.role

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