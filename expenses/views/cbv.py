from django.http import HttpResponse
from django.views import View

from django_oso.auth import authorize
from django_oso import Oso

class MyView(View):
    def get(self, request):
        authorize(request=request, resource="my_view")
        return HttpResponse('result')

from expenses.models import Expense
from django.views.generic import DetailView

class ExpenseView(DetailView):
    model = Expense
    queryset = Expense.objects.all()

    def get_object(self):
        expense = super().get_object()
        authorize(request=self.request, action="read", resource=expense)
        return expense
        
from django.views.generic import ListView

class ListExpenses(ListView):
    model = Expense

    def get_queryset(self):
        return Expense.objects.authorize(self.request, action="read")
