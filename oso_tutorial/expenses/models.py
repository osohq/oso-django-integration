import json
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.deletion import CASCADE
from django_oso.models import AuthorizedModel


class Expense(AuthorizedModel):
    # basic information
    amount = models.IntegerField()
    description = models.CharField(max_length=1024)

    # ownership/category
    owner = models.ForeignKey("User", CASCADE)
    category = models.ForeignKey("Category", CASCADE)

    # time info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def from_json(self, data):
        return self(**data)


class UserManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related("organizations")
            .prefetch_related("categories")
        )


class User(AbstractUser):
    # basic info
    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    manager = models.ForeignKey("User", models.SET_NULL, null=True)

    organizations = models.ManyToManyField("Organization", through="OrganizationMember")
    categories = models.ManyToManyField("Category", through="CategoryMember")

    objects = UserManager()


class Organization(AuthorizedModel):
    name = models.CharField(max_length=1024)
    members = models.ManyToManyField(User, through="OrganizationMember")


class Category(AuthorizedModel):
    name = models.CharField(max_length=1024)
    members = models.ManyToManyField(User, through="CategoryMember")
    organization = models.ForeignKey(Organization, on_delete=CASCADE)

    def __str__(self):
        return f"{self.name.title()} at {self.organization.name}"


class OrganizationMember(models.Model):
    organization = models.ForeignKey(Organization, on_delete=CASCADE)
    member = models.ForeignKey(User, on_delete=CASCADE)
    role = models.CharField(max_length=64, default="member")


class CategoryMember(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    member = models.ForeignKey(User, on_delete=CASCADE)
    role = models.CharField(
        max_length=64,
    )

    def __str__(self):
        return f"{self.role.title()} for {self.category}"