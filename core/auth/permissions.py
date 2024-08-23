from rest_framework.permissions import BasePermission, SAFE_METHODS

# NOT IN BOOK, SUGGESTED BY CHATGPT
class UserPermission(BasePermission):

    def has_permission(self, request, view):
        # Allow read-only access to anonymous users
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        # Check if the user is authenticated for all other views
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow superusers to access any object
        if request.user.is_superuser:
            return True

        # Handle permissions for posts
        if view.basename == 'post':
            if request.method in ['PUT', 'DELETE', 'PATCH']:
                return obj.author == request.user
            if request.method in SAFE_METHODS:
                return True
            return False

        # Handle permissions for comments
        if view.basename == 'post-comment':
            if request.method == 'PUT':
                # Allow deleting comments authored by the user or the post's author
                return obj.author == request.user
            if request.method == 'DELETE':
                # Allow deleting comments if the user is the comment author or the post author
                return obj.author == request.user or obj.post.author == request.user
            if request.method in SAFE_METHODS:
                return True
            return False

        # Default deny for other cases
        return False