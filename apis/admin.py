from django.contrib import admin

from apis.models import Student, Drink, Employees, DrinkFeedback

# Register your models here.
admin.site.register(Student)
admin.site.register(Drink)
admin.site.register(Employees)
admin.site.register(DrinkFeedback)
