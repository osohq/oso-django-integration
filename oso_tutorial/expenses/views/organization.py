import json

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from expenses.models import Organization

def get_organization(request, id):
    organization = Organization.objects.get(pk=id)
    return HttpResponse(organization.json())
