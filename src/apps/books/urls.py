from django.urls import path
from . import views


urlpatterns = [
    path('', views.books, name='book-list'),
    path('create/', views.create_book, name='book-create'),
    path('<int:pk>/put/', views.put_book, name='book-put'),


]