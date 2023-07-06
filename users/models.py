from django.db import models

# Create your models here.
class Users(models.Model):

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Role(models.Model):

    role_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.role_name