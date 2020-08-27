from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def get_expense(request, id):
    return HttpResponse("expense 1")

@require_http_methods(["PUT"])
def submit_expense(request):
    return HttpResponse("expense submitted")
