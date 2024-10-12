from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
# from auth_app.views import RegisterAPIView, ProtectedAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('api/v1/register/', RegisterAPIView.as_view(), name='register'),
    # path('api/v1/protected/', ProtectedAPIView.as_view(), name='protected'),
]


