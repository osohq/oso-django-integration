import json

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_oso.auth import authorize
from django_oso.decorators import skip_authorization

from ..models import Expense

def list_expenses(request):
    expenses = Expense.objects.authorize(request, action="read")
    return render(request, "list.html", {"expenses": expenses})


def get_expense(request, id):
    try:
        expense = Expense.objects.get(pk=id)
    except Expense.DoesNotExist:
        return HttpResponseNotFound()

    authorize(request, expense, action="read")
    return HttpResponse(expense.json())

@require_http_methods(["PUT"])
def submit_expense(request):
    expense_data = json.loads(request.body)

    expense_data.setdefault("user_id", request.user.id)

    expense = Expense.from_json(expense_data)
    expense.save()

    return HttpResponse(json.dumps(expense.json()))
