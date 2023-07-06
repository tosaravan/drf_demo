from django.contrib import admin

# Register your models here.
from users.models import Users, Role


# Register your models here.
admin.site.register(Users)
admin.site.register(Role)