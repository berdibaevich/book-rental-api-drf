from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_api, name='login'),
    path('me/', views.me_api_view, name='user-me'),
]