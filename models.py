from django import models

class Expense(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()

    user = models.ForeignKey(User, models.CASCADE)
    description = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField()

class User(db.Model):
    id = models.IntegerField(primary_key=True)

    email = models.CharField()
    title = models.CharField()

    location_id = models.IntegerField()
    organization = models.ForeignKey(Organization, models.CASCADE)
    manager = models.ForeignKey('User', models.SET_NULL, null=True)
