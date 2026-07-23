from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list_create, name='book-list-create'),
]