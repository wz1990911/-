from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):

    #这是父类方法
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """


        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            if obj.operator == request.user:
                return True
            else:
                return False
