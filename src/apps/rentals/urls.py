from django.urls import path
from .views import (
    category_list
)


urlpatterns = [    
    # Category
    path('categories/', category_list, name='category-list-create'),
]