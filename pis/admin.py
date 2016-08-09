from django.contrib import admin

# Register your models here.
from schedules.models import Window
from .models import Pi

admin.site.register(Pi)
admin.site.register(Window)
