from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Attendance,AppUser

admin.site.register((Attendance,AppUser))
admin.site.unregister(Group)