from rest_framework import permissions

class IsBranchManagerOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Unauthenticated users & normal users → Can view api endpoints(read-only).
    - Branch_Manager users → Can perform all CRUD operations in api endpoints.
    """

    def has_permission(self, request, view):
        # Allow read-only access (GET, HEAD, OPTIONS) for everyone (even unauthenticated users)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write permissions only for users in the Branch_Manager group
        return request.user.is_authenticated and request.user.groups.filter(name="Branch_Manager").exists()

class IsBranchManager(permissions.BasePermission):
    """
    Custom permission:
    - Branch_Manager users → Can perform all CRUD operations in api endpoints.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Branch_Manager").exists()