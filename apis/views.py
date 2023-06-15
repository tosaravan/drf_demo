from django.shortcuts import render
from rest_framework import viewsets

from apis.models import Student
from apis.serializers import StudentsSerializer


# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Student.objects.all()

    # specify serializer to be used
    serializer_class = StudentsSerializer
