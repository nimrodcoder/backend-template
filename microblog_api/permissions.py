from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id

class UpdateOwnBlog(permissions.BasePermission):
    """ Allows user to edit their own blogs """

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit his own blog"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id==request.user.id

class UpdateOwnComment(permissions.BasePermission):
    """ Allows user to edit their own comments """
    
    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit his own comment"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id==request.user.id
