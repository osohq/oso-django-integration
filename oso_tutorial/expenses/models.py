from django.db import models

class Expense(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()

    user = models.ForeignKey('User', models.CASCADE)
    description = models.CharField(max_length=1024)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=1024)

    id = models.IntegerField(primary_key=True)

class User(models.Model):

    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    location_id = models.IntegerField()
    organization = models.ForeignKey(Organization, models.CASCADE)
    manager = models.ForeignKey('User', models.SET_NULL, null=True)
