from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # permissions.SAFE_METHODS : 읽기 전용 HTTP 메서드 목록 ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        obj = view.get_object(request, *view.args, **view.kwargs)
        return obj.author == request.user