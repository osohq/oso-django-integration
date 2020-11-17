from collections import defaultdict

import json
from django.db.models.query import Prefetch

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_oso import Oso
from django_oso.auth import authorize
from django_oso.decorators import skip_authorization

from ..apps import ExpensesConfig
from ..models import Category, Expense, Organization


def list_expenses(request):
    if ExpensesConfig.partial_enabled:
        organizations = Organization.objects.authorize(request, action="read")
        expenses = (
            (Expense.objects.authorize(request, action="read"))
            .prefetch_related(Prefetch("organization", queryset=organizations))
            .select_related("owner")
            .select_related("category")
            .order_by("category__name")
        )
    else:
        expenses = (
            (Expense.objects.all())
            .prefetch_related("organization")
            .select_related("owner")
            .select_related("category")
            .order_by("category__name")
        )
        expenses = filter(lambda e: Oso.is_allowed(request.user, "read", e), expenses)

    # group as a dict by category
    res = defaultdict(list)
    for expense in expenses:
        res[expense.category].append(expense)

    return render(request, "list.html", {"expenses": res.items()})


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
