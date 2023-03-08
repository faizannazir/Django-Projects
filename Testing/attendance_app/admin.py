from django.contrib import admin

# Register your models here.
from .models import Employee,Attendance,Leave

admin.site.register((Employee,Attendance,Leave))