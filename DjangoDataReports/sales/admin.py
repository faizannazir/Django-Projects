from django.contrib import admin

from .models import Position, Sale, CSV

# Register your models here.

admin.site.register([Position,Sale,CSV])