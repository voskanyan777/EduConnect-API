from rest_framework.permissions import BasePermission

class IsTeacherUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'teacher')