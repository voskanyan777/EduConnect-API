from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Course
from .serializers import CreateCourseSerializer

class CreateCourseAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer