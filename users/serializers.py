# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'mobile', 'postcode', 'country']