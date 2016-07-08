from django.db import models



class Schedule(models.Model):
    schedule_date = models.DateField()
    window = models.ForeignKey('pis.Window')

    def __str__(self):
        return self.schedule_date.strftime('%Y-%m-%d') + '  @ Pi:' + str(self.pi)

    class Meta:
        unique_together = (('schedule_date', 'window'),)

    def duplicate(self, new_date, new_window):
        """
        Duplicate the Schedule to a new date and/or time
        :param new_date:
        :param new_pi:
        :return:
        """


class ScheduleItem(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='items')
    video = models.ForeignKey('videos.Video')
    video_start_seconds = models.PositiveIntegerField(null=True, blank=True)
    video_duration_seconds= models.PositiveIntegerField(null=True, blank=True)
    start_time = models.TimeField()
