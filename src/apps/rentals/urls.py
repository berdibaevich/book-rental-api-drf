from django.urls import path
from .views import (
    CategoryListCreateAPIView
)


urlpatterns = [    
    # Category
    path('libraries/<slug:slug>/categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
]