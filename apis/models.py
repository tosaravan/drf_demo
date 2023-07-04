from django.db import models


# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " " + self.description


class Employees(models.Model):
    fullname = models.CharField(max_length=200)
    sex = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class DrinkFeedback(models.Model):

    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    feedback = models.CharField(max_length=2000)

    def __str__(self):
        return self.fullname + " " + self.email + " " + self.feedback


class Users(models.Model):

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname
