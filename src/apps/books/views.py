from rest_framework.decorators import api_view
from rest_framework import status, response

from .models import Book
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    BookCreateSerializer,
    BookUpdateSerializer
)


@api_view(['GET', 'POST'])
def book_list_create(request):
    match request.method:
        case "GET":
            books = Book.objects.all()
            serializers = BookListSerializer(books, many=True)
            return response.Response(data=serializers.data, status=status.HTTP_200_OK)

        case "POST":
            serializer = BookCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail_update_delete(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return response.Response(
            {'errors': 'Book not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    match request.method:
        case "GET": 
            serializer = BookDetailSerializer(book)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        
        case "PUT":
            serializer = BookUpdateSerializer(book, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response({'message': 'Book updated successfully.'}, status=status.HTTP_200_OK)
        
        case "PATCH":
            serializer = BookUpdateSerializer(book, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(
                {'message': 'Book updated successfully [PATCH].'},
                status=status.HTTP_200_OK
            )
        
        case "DELETE":
            book.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
