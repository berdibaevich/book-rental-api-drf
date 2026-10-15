from rest_framework.permissions import BasePermission

from src.utils.choices import Role
from ..models import Library


class IsOwnerLibrary(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated and request.user.role == Role.OWNER):
            return False
        
        slug = view.kwargs.get("slug")
        if not slug:
            return False
        
        return Library.objects.filter(slug=slug, owner=request.user).exists()