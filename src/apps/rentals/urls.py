from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView
)


urlpatterns = [    
    # Category
    path('libraries/<slug:slug>/categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('libraries/<slug:slug>/categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category_detail'),

]