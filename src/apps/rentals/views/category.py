from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from ..models import Category, Library
from ..serializers import (
    CategoryListCreateSerializer,
    CategoryDetailSerializer
)
from ..permissions import (
    IsOwnerLibrary
)



class CategoryListCreateAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(), )
        return (IsOwnerLibrary(), )


    def get(self, request, slug):
        categories = Category.objects.filter(library__slug = slug)
        serializers = CategoryListCreateSerializer(categories, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


    def post(self, request, slug):
        library = get_object_or_404(Library, slug=slug)
        serializer = CategoryListCreateSerializer(
            data=request.data, 
            many=True,
            allow_empty=False,
            context={'library': library}
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (IsOwnerLibrary, )
    lookup_field = 'id'


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['library'] = self.get_object().library
        return context