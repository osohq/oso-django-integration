import json
from django.contrib.auth.models import AbstractUser

from django.db import models
from django_oso.models import AuthorizedModel

class Expense(AuthorizedModel):
    amount = models.IntegerField()

    owner = models.ForeignKey('User', models.CASCADE)
    organization = models.ForeignKey('Organization', models.CASCADE)
    description = models.CharField(max_length=1024)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def json(self):
        return json.dumps({
            'id': self.id,
            'amount': self.amount,
            'user_id': self.user.id,
            'description': self.description
        })

    @classmethod
    def from_json(self, data):
        return self(**data)



class User(AbstractUser):
    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    location_id = models.IntegerField()
    organizations = models.ManyToManyField('Organization', through='OrganizationMember')
    categories = models.ManyToManyField('Category', through='CategoryMember')

    manager = models.ForeignKey('User', models.SET_NULL, null=True)

    def json(self):
        return json.dumps({
            'id': self.id,
            'email': self.email,
            'title': self.title,
            'location_id': self.location_id,
            'organization': self.organization.id,
        })

class Category(models.Model):
    name = models.CharField(max_length=1024)
    members = models.ManyToManyField(User, through='CategoryMember')


class Organization(AuthorizedModel):
    name = models.CharField(max_length=1024)
    members = models.ManyToManyField(User, through='OrganizationMember')

    def json(self):
        return json.dumps({
            'id': self.id,
            'name': self.name
        })

class OrganizationMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=64, default="member", choices=[("member", "Member"), ("owner", "Owner")])

class CategoryMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)