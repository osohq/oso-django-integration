# Top-level rules

allow(user, "GET", "my_view");
allow(user, "read", expense: expenses::Expense) if expense.id = 1;

allow(_user: expenses::User, "GET", http_request: HttpRequest) if
    http_request.path = "/whoami/";

# Allow by path segment
allow(user, action, http_request: HttpRequest) if
    http_request.path.strip("/").split("/") = [stem, *rest]
    and allow_by_path(user, action, stem, rest);

### Expense rules

# by HTTP method
allow_by_path(_user, "GET", "expenses", _rest);
allow_by_path(_user, "PUT", "expenses", ["submit"]);

# by model
allow(user: expenses::User, "read", expense: Expense) if
    submitted(user, expense);

submitted(user: expenses::User, expense: Expense) if
    user.id = expense.user_id;

### Organization rules
allow_by_path(_user, "GET", "organizations", _rest);
allow(user: expenses::User, "read", organization: Organization) if
    user.organization_id = organization.id;
