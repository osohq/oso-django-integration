user_in_role(user, role, resource) if
    not ExpensesConfig.partial_enabled and
    reg_user_in_role(user, role, resource);

# CEOs are viewers
reg_user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    e.category.organization in user.organizations.all() and
    user.title = "CEO";

# org member
reg_user_in_role(user: expenses::User, "member", org: expenses::Organization) if
    org in user.organizations.all() and
    org.organizationmember__role = "member";

# category auditor
reg_user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
    expense.category in user.categories.filter(categorymember__role: "auditor");
