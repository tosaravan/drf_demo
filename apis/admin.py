from django.contrib import admin

from apis.models import Student, Drink, Employees, DrinkFeedback, Users

# Register your models here.
admin.site.register(Student)
admin.site.register(Drink)
admin.site.register(Employees)
admin.site.register(DrinkFeedback)
admin.site.register(Users)

