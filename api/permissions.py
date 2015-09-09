from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print 'Aqui2'
        return self.has_object_permision(request, view)

    def has_object_permision(self, request, view, obj=None):
        print 'Aqui'
        return request.method in permissions.SAFE_METHODS


class PostAuthorCanEditPermission(SafeMethodsOnlyPermission):
    def has_object_permision(self, request, view, obj=None):
        if obj is None:
            can_edit = True
            print 'yres'
        else:
            can_edit = request.user == obj.author
            print 'post'

        return can_edit or super(PostAuthorCanEditPermission, self).has_object_permision(request, view, obj)
