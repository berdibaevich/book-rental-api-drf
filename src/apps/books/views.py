from rest_framework.decorators import api_view
from rest_framework import status, response

from .models import Category, Book


@api_view(['GET'])
def books(request):
    if request.method == "GET":
        books = Book.objects.values('id', 'title', 'description')
        return response.Response(data=books, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_book(request):
    data = request.data
    # Step 1
    if not data:
        return response.Response(
            {'errors': 'Sorry, request body is empty!'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Step 2
    title = data.get('title')
    desc = data.get('description')
    category_ids = data.get('category_ids')

    errors = {}

    if title is None or str(title).strip() == '':
        errors['title'] = ['This field is required']
    
    if category_ids is None or not isinstance(category_ids, list):
        errors['category_ids'] = ['Category IDs are required!']

    existing_categories = Category.objects.filter(id__in = category_ids)

    if len(existing_categories) != len(set(category_ids)):
        errors['category_ids'] = ['Some category IDs do not exists.']
    

    if errors:
        return response.Response(
            {'errors': errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    

    new_book = Book.objects.create(
        title=title,
        description=desc,
    )
    new_book.categories.set(category_ids)

    return response.Response({'id': new_book.id, 'title': new_book.title}, status=status.HTTP_201_CREATED)