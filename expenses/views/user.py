import json

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from django_oso.decorators import authorize_request

from expenses.models import Organization, User

@authorize_request
def whoami(request):
    user = request.user
    if isinstance(user, User):
        organization = user.organization.name
        return HttpResponse(f"You are {user.email}, the {user.title} at {organization}. (User ID: {user.id})")
    else:
        return HttpResponse("You are a guest.")
