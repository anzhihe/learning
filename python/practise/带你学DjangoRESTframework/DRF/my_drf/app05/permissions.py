from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False

        return True
