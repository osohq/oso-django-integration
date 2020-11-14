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


# Users can see their own organizations
allow(user: expenses::User, "read", organization: expenses::Organization) if
    in_org(organization, user);


allow(user: expenses::User, "read", category: expenses::Category) if
    in_category(user, category);

# Partial supported: use partial lookup on ID
in_org(org, obj) if
    ExpensesConfig.partial_enabled and
    org.id in obj.organizations.values_list("id", flat: true);

# Partials not supported: use django iterator
in_org(org, obj) if
    not ExpensesConfig.partial_enabled and
    org in obj.organizations.all();

# Partial supported: use partial lookup on ID
# in_category(obj, cat) if
#     ExpensesConfig.partial_enabled and
#     cat.members = obj;

# # Partials not supported: use django iterator
# in_category(obj, cat) if
#     not ExpensesConfig.partial_enabled and
#     cat in obj.organizations.all();