from rest_framework.permissions import BasePermission
from ..models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Admins').exists():
            return True
        return False