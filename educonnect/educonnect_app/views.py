from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import Course
from .serializers import CreateCourseSerializer
from .permissions import IsTeacherUser

class CreateCourseView(CreateAPIView):
    def post(self, request):
        serializer = CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            course = Course.objects.create(
                name=serializer.data['name'],
                description=serializer.data['description'],
                available_groups=serializer.data['available_groups'],
                created_by_teacher=request.user,
            )
            course.save()
            return Response({
                "data": serializer.data,
            }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsTeacherUser, )