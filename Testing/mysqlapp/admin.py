from django.contrib import admin
from .models import Registeration , Reg
# Register your models here.


admin.site.register(Registeration, admin.ModelAdmin)
admin.site.register(Reg)