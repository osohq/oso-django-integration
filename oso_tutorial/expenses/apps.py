from django.apps import AppConfig

from django_oso import Oso


class ExpensesConfig(AppConfig):
    name = "expenses"

    partial_enabled = False

    def ready(self):
        Oso.register_class(ExpensesConfig)
