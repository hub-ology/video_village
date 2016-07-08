from django.contrib import admin

from schedules.models import ScheduleItem, Schedule

admin.site.register(Schedule)
admin.site.register(ScheduleItem)
