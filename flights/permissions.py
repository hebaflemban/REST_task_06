from rest_framework import permissions
from django.utils import timezone
class IsOwner(permissions.BasePermission):
    message = 'not allowed'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_staff:
            return True
        else:
            return False


class Is3Away(permissions.BasePermission):
    message = 'Too late'

    def has_object_permission(self, request, view, obj):
        if (obj.date - timezone.now().date()).days > 3 :
            return True
        else:
            return False
