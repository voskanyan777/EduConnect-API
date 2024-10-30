from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Course
from .serializers import CreateCourseSerializer, CreateTaskSerializer
from .permissions import IsTeacher

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

    permission_classes = (IsTeacher, )


class CreateTaskView(generics.CreateAPIView):
    serializer_class = CreateTaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    permission_classes = (IsTeacher, )