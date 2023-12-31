from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis.models import Student, Drink, Employees
from apis.serializers import StudentsSerializer, DrinkSerializer, EmployeesSerializer
from .models import Drink, Employees


# Create your views here.
# class based view for Student
class StudentsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Student.objects.all()

    # specify serializer to be used
    serializer_class = StudentsSerializer


# function based view for drinks
@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializers = DrinkSerializer(drinks, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# function view to get a specific drink based on the id
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk):
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(Drink, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesViewSet(viewsets.ModelViewSet):

    queryset = Employees.objects.all()

    serializer_class = EmployeesSerializer

