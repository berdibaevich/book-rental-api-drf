from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from ..models import Category
from ..serializers import (
    CategoryListSerializer
)
from ..permissions import (
    IsOwnerLibrary
)


@api_view(['GET'])
@permission_classes([IsOwnerLibrary])
def category_list(request):
    categories = Category.objects.filter(library__owner = request.user)
    serializers = CategoryListSerializer(categories, many = True)
    return Response(data=serializers.data, status=status.HTTP_200_OK)

