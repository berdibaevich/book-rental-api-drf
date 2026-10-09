from rest_framework.permissions import BasePermission

from src.utils.choices import Role


class IsOwnerLibrary(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and
            request.user.role == Role.OWNER
            )
