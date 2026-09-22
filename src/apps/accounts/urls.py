from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up_api, name='sign-up'),
    path('login/', views.login_api, name='login'),
    path('me/', views.me_api_view, name='user-me'),
]