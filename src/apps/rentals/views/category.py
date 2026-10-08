from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Category
from ..serializers import (
    CategoryListSerializer
)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializers = CategoryListSerializer(categories, many = True)
    return Response(data=serializers.data, status=status.HTTP_200_OK)

