# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

from . import views
# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'students', StudentsViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('drinks/',views.drink_list),
    path('drinks/<int:pk>/',views.drink_detail),
]
