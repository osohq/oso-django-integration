### Expense app authorization policy

allow(user, action, resource) if
    rbac_allow(user, action, resource);

# RBAC policy structure
rbac_allow(user: expenses::User, action, resource) if
    user_in_role(user, role, resource) and
    role_allow(role, action, resource);

### Two roles: viewer, manager

# Viewer

role_allow("viewer", "read", _: expenses::Expense);

# expense submitters are viewers
user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    user = e.owner;

# CEOs are viewers
user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    e.organization in user.organizations.all() and
    user.title = "CEO";


# Members can see their own organizations
role_allow("member", "read", _: expenses::Organization);

# Partials supported: use partial lookup on ID
user_in_role(user: expenses::User, role, org: expenses::Organization) if
    ExpensesConfig.partial_enabled and
    org.id in user.organizations.values_list("id", flat: true) and
    org.organizationmember__role = role;

# Partials not supported: use django iterator
user_in_role(user: expenses::User, role, org: expenses::Organization) if
    not ExpensesConfig.partial_enabled and
    org in user.organizations.all() and
    org.organizationmember__role = role;


role_allow("auditor", "read", _: expenses::Organization);
role_allow("auditor", "read", _: expenses::Expense);

user_in_role(user: expenses::User, "auditor", org: expenses::Organization) if
    ExpensesConfig.partial_enabled and
    org.id in user.categories.filter(categorymember__role: "auditor").values_list("organization_id", flat: true);

user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
    ExpensesConfig.partial_enabled and
    expense.category in user.categories.filter(categorymember__role: "auditor");

user_in_role(user: expenses::User, "auditor", org: expenses::Organization) if
    not ExpensesConfig.partial_enabled and
    org in user.categories.filter(categorymember__role: "auditor").all();

user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
    not ExpensesConfig.partial_enabled and
    user in expense.category.members.filter(categorymember__role: "auditor");
