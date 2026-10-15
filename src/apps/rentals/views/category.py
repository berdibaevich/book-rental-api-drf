from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from ..models import Category
from ..serializers import (
    CategoryListSerializer
)
from ..permissions import (
    IsOwnerLibrary
)



class CategoryListCreateAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, slug):
        categories = Category.objects.filter(library__slug = slug)
        serializers = CategoryListSerializer(categories, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


