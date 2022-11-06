from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of a room
        return obj.owner == request.user
