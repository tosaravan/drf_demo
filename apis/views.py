from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis.models import Student, Drink, Employees, DrinkFeedback, Users
from apis.serializers import StudentsSerializer, DrinkSerializer, EmployeesSerializer, DrinksFeedbackSerializer, UserSerializer
from .models import Drink, Employees, DrinkFeedback, Users


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
        serializer = DrinkSerializer(drink, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesViewSet(viewsets.ModelViewSet):

    queryset = Employees.objects.all()

    serializer_class = EmployeesSerializer


@api_view(['GET', 'POST'])
def drink_feedback(request):
    if request.method == 'GET':
        drinks_feedback = DrinkFeedback.objects.all()
        serializers = DrinksFeedbackSerializer(drinks_feedback, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = DrinksFeedbackSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# function view to get a specific drinks feedback with ID
@api_view(['GET', 'PUT', 'DELETE'])
def drink_feedback_detail(request, pk):

    try:
        drink_feedback = DrinkFeedback.objects.get(pk=pk)
    except DrinkFeedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinksFeedbackSerializer(drink_feedback)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinksFeedbackSerializer(drink_feedback, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink_feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):

    try:
        users = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(users, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)