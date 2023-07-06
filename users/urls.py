# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

from .import views

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

urlpatterns = [
    path('users/', views.users),
    path('users_detail/<int:pk>/', views.users_detail),
    path('role/', views.role),
    path('role_detail/<int:pk>/', views.role_detail),
]

