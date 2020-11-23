### oso demo

# users can see their own expenses
allow(user: expenses::User, "read", expense: expenses::Expense) if
    user = expense.owner;

allow(user: expenses::User, "read", org: expenses::Organization) if
    org in user.organizations.all();

# users can see expenses in their organization

user_in_org(user, organization) if
    user in organization.members;

allow(user: expenses::User, "read", expense: expenses::Expense) if
    user_in_org(user, expense.category.organization)
    and user.title = "CEO";

# users can see expenses that they are the auditor for

user_in_cat_role(user, role_name, category) if
    cm in category.categorymember and
    cm.role = role_name and
    cm.member = user;

allow(user: expenses::User, "read", expense: expenses::Expense) if
    user_in_cat_role(user, "auditor", expense.category);

