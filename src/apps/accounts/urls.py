from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    signup_api,
    me_api,
    tokenObtainPairView
)


urlpatterns = [
    path('signup/', signup_api, name='signup'),
    path('token/', tokenObtainPairView, name='token_obtain_pair'),        
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', me_api, name='me'),
]