from django.db import models


class Schedule(models.Model):
    schedule_date = models.DateField()
    pi = models.PositiveIntegerField()


class ScheduleItem(models.Model):
    schedule = models.ForeignKey(Schedule)
    video = models.ForeignKey('videos.Video')
    video_start_seconds = models.PositiveIntegerField(null=True, blank=True)
    video_stop_seconds = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.TimeField()
