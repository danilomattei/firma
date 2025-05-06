from django.contrib import admin

# Register your models here.
from .models import Employee, Department, Attendance

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Attendance)
