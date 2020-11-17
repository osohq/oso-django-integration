### Expense app authorization policy

allow(user, action, resource) if
    rbac_allow(user, action, resource);

# RBAC policy structure
rbac_allow(user: expenses::User, action, resource) if
    user_in_role(user, role, resource) and
    role_allow(role, action, resource);

### Three roles: expense viewer, org member, org/category auditor

# Members can see their own organizations
role_allow("member", "read", _: expenses::Organization);

# Expense viewers and auditors
role_allow("viewer", "read", _: expenses::Expense);
role_allow("auditor", "read", _: expenses::Expense);

# expense submitters are viewers
user_in_role(user: expenses::User, "viewer", e: expenses::Expense) if
    user = e.owner;
