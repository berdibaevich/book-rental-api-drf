from rest_framework.decorators import api_view
from rest_framework import status, response

from .models import Category, Book


@api_view(['GET'])
def books(request):
    if request.method == "GET":
        books = Book.objects.values('id', 'title', 'description')
        return response.Response(data=books, status=status.HTTP_200_OK)
