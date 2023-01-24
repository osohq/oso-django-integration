# Top-level rules

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
allow_by_path(_user, _method, "admin", _rest);

# by model
allow(user: expenses::User, "read", expense: expenses::Expense) if
    submitted(user, expense);

submitted(user: expenses::User, expense: expenses::Expense) if
    user.id = expense.user_id;

### Organization rules
allow_by_path(_user, "GET", "organizations", _rest);
allow(user: expenses::User, "read", organization: expenses::Organization) if
    user.organization_id = organization.id;
