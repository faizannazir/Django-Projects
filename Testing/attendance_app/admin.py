from django.contrib import admin

# Register your models here.
from .models import Employee,Attendance

admin.site.register((Employee,Attendance))