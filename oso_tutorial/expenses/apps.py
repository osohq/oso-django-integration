from django.apps import AppConfig

from django_oso import Oso


class ExpensesConfig(AppConfig):
    name = "expenses"

    partial_enabled = True

    def ready(self):
        Oso.register_class(ExpensesConfig)
