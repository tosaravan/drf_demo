from django.contrib import admin

from apis.models import Student, Drink, Employee, DrinkFeedback

# Register your models here.
admin.site.register(Student)
admin.site.register(Drink)
admin.site.register(Employee)
admin.site.register(DrinkFeedback)


