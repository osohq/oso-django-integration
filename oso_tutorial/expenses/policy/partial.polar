# user_in_role(user, role, resource) if
#     ExpensesConfig.partial_enabled and
#     partial_user_in_role(user, role, resource);

# # CEOs are viewers
# partial_user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
#     e.category in expenses::Category.objects.filter(organization__in: user.organizations.all()) and
#     user.title = "CEO";

# # org member
# partial_user_in_role(user: expenses::User, "member", org: expenses::Organization) if
#     ExpensesConfig.partial_enabled and
#     org.id in user.organizations.filter(organizationmember__role: "member").values_list("id", flat: true);

# # category auditor
# partial_user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
#     ExpensesConfig.partial_enabled and
#     expense.category in user.categories.filter(categorymember__role: "auditor");

