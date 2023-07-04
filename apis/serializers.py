# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Student, Drink, Employees, DrinkFeedback, Users


# Create a model serializer
class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Student
        fields = ('fullname', 'email')


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model= Drink
        fields = ['id', 'name', 'description']


class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ['fullname', 'sex']


class DrinksFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrinkFeedback
        fields = ['id', 'fullname', 'email', 'feedback']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'mobile', 'postcode', 'country']

