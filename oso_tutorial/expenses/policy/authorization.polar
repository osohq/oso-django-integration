allow(user: User, "read", expense: Expense) if
    submitted(user, expense);

submitted(user: User, expense: Expense) if
    user.id = expense.user_id;
