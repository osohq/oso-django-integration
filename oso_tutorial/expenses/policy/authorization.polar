# allow rule to enable role checking
allow(actor, action, resource) if
    user_in_role(actor, role, resource) and
    role_allow(role, action, resource);

role_allow("member", "read", _organization: expenses::Organization);

# get user role from OrganizationMember relation
user_in_role(user: expenses::User, role, organization: expenses::Organization) if
    user = organization.members and
    organization.organizationmember__role = role;

allow(user: expenses::User, "read", expense: expenses::Expense) if
    user_in_role(user, "member", expense.category) and
    user_in_role(user, "member", expense.organization);
