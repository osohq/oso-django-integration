from django.core.exceptions import PermissionDenied

from .oso import Oso

def authorize(request, resource, *, actor=None, action=None):
    if actor is None:
        actor = request.user

    if action is None:
        action = request.method

    if not Oso.is_allowed(actor, action, resource):
        raise PermissionDenied()
