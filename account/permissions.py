from rest_framework.permissions import BasePermission


class IsActivePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_active


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj == request.user
