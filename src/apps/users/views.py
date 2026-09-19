from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, response
from rest_framework.authtoken.models import Token

from .serializers import (
    LoginSerializer,
    UserProfileSerializer
)


@api_view(['POST'])
def login_api(request):
    serializer = LoginSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)

    return response.Response(data={
        'token': token.key,
        'user_id': user.id,
        'username': user.username
    }, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_api_view(request):
    match request.method:
        case 'GET':
            serializer = UserProfileSerializer(request.user)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)