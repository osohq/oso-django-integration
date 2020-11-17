### Expense app authorization policy

allow(user, action, resource) if
    rbac_allow(user, action, resource);

# RBAC policy structure
rbac_allow(user: expenses::User, action, resource) if
    user_in_role(user, role, resource) and
    role_allow(role, action, resource);

### Three roles: 


# Members can see their own organizations
role_allow("member", "read", _: expenses::Organization);
# Auditors can see organizations they audit
role_allow("auditor", "read", _: expenses::Organization);

# Expense viewers and auditors
role_allow("viewer", "read", _: expenses::Expense);
role_allow("auditor", "read", _: expenses::Expense);

# Viewer

# expense submitters are viewers
user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    user = e.owner;

# CEOs are viewers
user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    ExpensesConfig.partial_enabled and
    e.category in expenses::Category.objects.filter(organization__in: user.organizations.all()) and
    user.title = "CEO";

# Partials supported: use partial lookup on ID
user_in_role(user: expenses::User, "member", org: expenses::Organization) if
    ExpensesConfig.partial_enabled and
    org.id in user.organizations.filter(organizationmember__role: "member").values_list("id", flat: true);

user_in_role(user: expenses::User, "auditor", org: expenses::Organization) if
    ExpensesConfig.partial_enabled and
    # The values_list part is a workaround for `org in user.categories.filter(organizationmember__role: "auditor")`
    org.id in user.organizations.filter(organizationmember__role: "auditor").values_list("id", flat: true);

user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
    ExpensesConfig.partial_enabled and
    expense.category in user.categories.filter(categorymember__role: "auditor");


# Partials not supported: use django iterator
user_in_role(user: expenses::User, role, org: expenses::Organization) if
    not ExpensesConfig.partial_enabled and
    org in user.organizations.all() and
    org.organizationmember__role = role;

user_in_role(user: expenses::User, "auditor", expense: expenses::Expense) if
    not ExpensesConfig.partial_enabled and
    expense.category in user.categories.filter(categorymember__role: "auditor");
