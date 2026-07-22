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


@api_view(['PUT'])
def put_book(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return response.Response(
            {'errors': 'Book not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    data = request.data
    errors = {}

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