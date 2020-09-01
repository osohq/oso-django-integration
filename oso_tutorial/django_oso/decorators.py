import functools

from . import auth

def skip_authorization(view_func):
    """View-decorator that marks a view as not requiring authorization.

    Use in combination with :py:func:`django_oso.middleware.RequireAuthorization`.
    Some views will not require authorization.  This decorator marks those views
    so that the middleware can skip the check.
    """
    @functools.wraps(view_func)
    def wrap_view(request, *args, **kwargs):
        auth.skip_authorization(request)
        return view_func(request, *args, **kwargs)

    return wrap_view
