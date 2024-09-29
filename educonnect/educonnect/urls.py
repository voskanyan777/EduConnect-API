from django.contrib import admin
from django.urls import path
from educonnect_app.views import CreateCourseAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/create-courses', CreateCourseAPIView.as_view())
]

