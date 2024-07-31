
from django.urls import path, include
from django.urls import re_path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)


urlpatterns = [
    path('', include('djoser.urls')),
    re_path(r"^jwt/create/?", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", CustomTokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", CustomTokenVerifyView.as_view(), name="jwt-verify"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
  
