from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list_create, name='book-list-create'),
    path('books/<int:pk>/', views.book_detail_update_delete, name='book-detail'),
    
    path('categories/', views.category_list_create, name='category-list-create'),
]