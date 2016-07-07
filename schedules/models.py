from django.db import models


class Schedule(models.Model):
    schedule_date = models.DateField()
    pi = models.PositiveIntegerField()

    def __str__(self):
        return self.schedule_date.strftime('%Y-%m-%d') + '  @ Pi:' + str(self.pi)


class ScheduleItem(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='items')
    video = models.ForeignKey('videos.Video')
    video_start_seconds = models.PositiveIntegerField(null=True, blank=True)
    video_stop_seconds = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.TimeField()
