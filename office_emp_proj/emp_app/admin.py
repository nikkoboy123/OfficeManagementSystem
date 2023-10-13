from django.contrib import admin
from .models import Employee,Role,Depart
# Register your models here.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Depart)