from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Employee,Attendance

admin.site.register((Employee,Attendance))
admin.site.unregister(Group)