from django.core.exceptions import PermissionDenied
from functools import wraps

def user_is_owner_or_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, username, *args, **kwargs):
        if request.user.is_superuser or request.user.username == username:
            return view_func(request, username, *args, **kwargs)
        raise PermissionDenied("شما اجازه دسترسی به این صفحه را ندارید.")
    return _wrapped_view
