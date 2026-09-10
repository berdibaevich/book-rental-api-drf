from rest_framework.decorators import api_view
from rest_framework import status, response

from .models import Category, Book
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    BookCreateSerializer
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
    
    data = request.data
    errors = {}

    match request.method:
        case "GET": 
            serializer = BookDetailSerializer(book)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    if ...:
        pass

    elif request.method == 'PUT':
        if 'title' not in data or data.get('title') is None or not str(data.get('title')).strip():
            errors['title'] = ['This field cannot be null or empty.']

        if 'description' not in data:
            errors['description'] = ['This field is required.']
        
        if 'category_ids' not in data or not isinstance(data.get('category_ids'), list):
            errors['category_ids'] = ['This field is required and must be a list of IDs.']

        if errors:
            return response.Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


        category_ids = data.get('category_ids')
        existing_categories = []

        if category_ids:
            existing_categories = Category.objects.filter(id__in=category_ids)
            if len(existing_categories) != len(set(category_ids)):
                return response.Response(
                    {'errors': 'Some category IDs dont exist.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            

        book.title = data['title']
        book.description = data['description']
        book.save()

        book.categories.set(existing_categories)

        return response.Response({'message': 'Book updated successfully.'}, status=status.HTTP_200_OK)


    elif request.method == 'PATCH':
        if 'title' in data:
            if (title_val := data.get('title')) is None or not str(title_val).strip():
                errors['title'] = ['This field cannot be null or empty!']   
            else:
                book.title = title_val

        if 'description' in data:
            book.description = data.get('description')

        if 'category_ids' in data:
            if not isinstance(category_ids := data.get('category_ids'), list):
                errors['category_ids'] = ['category_ids must be a list of integers.']
            
            elif category_ids:
                existing_categories = Category.objects.filter(id__in = category_ids)
                if len(existing_categories) != len(set(category_ids)):
                    errors['category_ids'] = ['Some category IDs dont exist.']
                else:
                    book.categories.set(category_ids)
            else:
                book.categories.clear()
        
        if errors:
            return response.Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        book.save()

        return response.Response(
            {'message': 'Book updated successfully [PATCH].'},
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        book.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
