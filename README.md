# oso: authorization as code [Django Integration Example]

oso allows you to write policy as code, tightly integrated
with application code, logic, and data, and provides a simple
way to enforce authorization on all requests.

## Example

This repository contains an example application using oso
and the oso Django integration to secure requests.

The application itself is a simple Django
web server, implementing an expenses application.

We used the ``oso`` & ``django-oso`` libraries.


## Test data

Load the fixture data with ``./manage.py loaddata expenses/fixtures/new_data.yaml``

You have:

- Alice, the CEO of Bar, Inc can see all Bar expenses
- Other users can see their own expenses
- Frantz is the Food auditor and can see all Food expenses for Foo and Bar
