from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list_create, name='book-list-create'),
    path('<int:pk>/', views.book_detail_update_delete, name='book-detail'),
]