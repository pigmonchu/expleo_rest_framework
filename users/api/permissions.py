from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Validar si el usuario que viene en request tiene acceso a la vista.
        Se pueden considerar los metodos
        """
        if request.method == "POST":
            return True
        elif request.user.is_superuser:
            return True
        elif view.__class__.__name__ == "UserDetailAPI":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        valida si el usuario que viene en request tiene acceso a la vista y permisos
        para manipular el obj
        """
        return request.user.is_superuser or request.user == obj

        return True
            
