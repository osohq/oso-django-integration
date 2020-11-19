### Expense app authorization policy

### Step 1: Simple ABAC

# # expense submitters are viewers
# allow(user: expenses::User, "read", e: expenses::Expense) if
#     user = e.owner;

### Step 2: RBAC

# allow(user, action, resource) if
#     rbac_allow(user, action, resource);

# # RBAC policy structure
# rbac_allow(user: expenses::User, action, resource) if
#     user_in_role(user, role, resource) and
#     role_allow(role, action, resource);

# ### Three roles: expense viewer, org member, org/category auditor

# # Members can see their own organizations
# role_allow("member", "read", _: expenses::Organization);

# # Expense viewers and auditors
# role_allow("viewer", "read", _: expenses::Expense);
# role_allow("auditor", "read", _: expenses::Expense);

