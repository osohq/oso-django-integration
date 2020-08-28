import json

from django.db import models

class Expense(models.Model):
    amount = models.IntegerField()

    user = models.ForeignKey('User', models.CASCADE)
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

class Organization(models.Model):
    name = models.CharField(max_length=1024)

class User(models.Model):
    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    location_id = models.IntegerField()
    organization = models.ForeignKey(Organization, models.CASCADE)
    manager = models.ForeignKey('User', models.SET_NULL, null=True)
