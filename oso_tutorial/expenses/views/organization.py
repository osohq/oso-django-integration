import json

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from django_oso.auth import authorize

from ..models import Organization
from ..apps import ExpensesConfig


def get_organization(request, id):
    if ExpensesConfig.partial_enabled:
        organization = Organization.objects.authorize(request, action="read").get(pk=id)
    else:
        organization = Organization.objects.get(pk=id)
        authorize(request, organization, action="read")
    return HttpResponse(organization.json())
