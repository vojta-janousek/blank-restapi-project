from rest_framework import permissions


class BlacklistPermission(permissions.BasePermission):
    '''Global permission check for blacklisted IPs.'''
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class AnonPermissionOnly(permissions.BasePermission):
    '''Non-authenticated users only'''
    message = 'You are already authenticated. Please log out to try again.'
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Object-level permission to only allow owner of an object to edit it.
    Assumes the model instance has an 'owner' attribute.
    '''
    message = 'You must be the owner of the status to change it.'
    def has_object_permission(self, request, view, obj):
        '''Read permissions are allowed to any request.'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
