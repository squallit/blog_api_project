from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    # Allow users to edit only their own profile

    def has_object_permission(self, request, view, obj):
        # Check to see if user tries to edit his own UserProfile

        # SAFE_METHODS are undestructive method such as GET, POST
        if request.method in permissions.SAFE_METHODS:
            return True

        # if Method is not safe such as UPDATE, DELETE
        # check if the currently authenticated user is the profile he is trying to change
        return obj.id == request.user.id
