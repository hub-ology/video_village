"""
Models associated with "shows."

A schedule is a sequence of schedule items.
Each schedule item comprises a date, time, and a show.
A show is a collection of window shows, where a window show
associates a window and a sequence of videos (a "playlist")
to be displayed in that window. A playlist is a sequence of
video segments to be shown, where a video segment could be
either a complete video or an excerpt specified as a start
second and a duration (in seconds).

An artist can set up a playlist. A playlist can be used many times.
A show can be used many times, too. For example, the same show
might run for three nights in a row--the artist would create one
show and then associate it with three schedule items.
"""


from django.db import models
from videos.models import Video
from django.utils.timezone import now
from datetime import time


class Window(models.Model):
    """
    A window is associated with a pi, a projector, and a screen
    """
    building = models.PositiveIntegerField()
    pi = models.ForeignKey('pis.Pi', null=True, blank=True)
    description = models.CharField(max_length=64, default="?")

    def __str__(self):
        return "Building {} - {}".format(self.building, self.description)

    class Meta(object):
        ordering = ('building',)


class Playlist(models.Model):
    """
    A playlist is a sequence of video segmentss to be played

    Note: The order in which videos play is determined by
    the offset_in_playlist for each video segment in the
    playlist. Care must be taken to ensure that video segments
    do not overlap in a playlist. A gap between two consecutive
    videos is handled by specifying an offset_in_playlist for the
    second video that is greater than the sum of offset_in_playlist
    and duration for the first video.
    """
    title = models.CharField(max_length = 255, blank=True)
    notes = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title


class VideoSegment(models.Model):
    """
    A video segment is a portion of a video that is characterized by three things:
        1. offset (in seconds) within the playlist to start showing this video
        2. offset (in seconds) in the video to start play
        3. duration (in seconds) to play the video
    """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    offset_in_playlist = models.PositiveIntegerField(help_text="The number of seconds from the start of the playlist to begin playing a video")
    offset_in_video = models.PositiveIntegerField(default=0, help_text="The number of seconds from the start of the video to begin playing")
    duration = models.PositiveIntegerField(help_text="the length of the video to play (in seconds)")
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return "[{:>5}] {} - Segment offset {}, duration {} on playlist {}".format(self.offset_in_playlist, self.video, self.offset_in_video, self.duration, self.playlist)


    class Meta(object):
        ordering = ('offset_in_playlist',)


class Show(models.Model):
    """
    A show is a collection of window shows.
    """
    notes = models.TextField(default="")

    def __str__(self):
        return "{:4}: {}".format(self.id, self.notes)


class WindowShow(models.Model):
    """
    A show is a display of videos that starts on a given date and a given time.
    A show is associated with a playlist that might repeat.
    """
    show = models.ForeignKey(Show, on_delete=models.CASCADE, help_text="The show this is a part of")
    window = models.ForeignKey(Window, on_delete=models.CASCADE, help_text="The window to be used")
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, help_text="The playlist to display in this window")
    offset_in_show = models.PositiveIntegerField(default=0, help_text="The number of seconds from the start of the show to delay playing this playlist in this window")
    repeats = models.PositiveIntegerField(default=1, help_text="The number of times to play the playlist (e.g., 1 means play it once)")

    def __str__(self):
        return "{}: {} [offset {}] {} (repeats: {})".format(self.window, self.show, self.offset_in_show,
                                                            (self.playlist), self.repeats)

    class Meta(object):
        ordering = ('show', 'offset_in_show', )


class ScheduleItem(models.Model):
    """
    A schedule item is a sequence of shows, each associated with a date and time to start.
    """

    date = models.DateField(default=now, help_text="The date of a show")
    time = models.TimeField(default=time(0, 0, 0), help_text="The time a show starts")
    show = models.ForeignKey(Show, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} - Show id {}".format(self.date, self.time, str(self.show))

    class Meta(object):
        ordering = ('date', 'time', )

# from django.db import models
#
#
# class Window(models.Model):
#     building = models.PositiveIntegerField()
#     pi = models.ForeignKey('pis.Pi', null=True, blank=True)
#
#
# class Showtime(models.Model):
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#
# class Schedule(models.Model):
#     schedule_start_date = models.DateField()
#     schedule_end_date = models.DateField()
#     repeat = models.BooleanField(default=False)
#     start_delay = models.BigIntegerField(default=0, blank=True)
#     window = models.ForeignKey(Window)
#
#     def __str__(self):
#         return self.schedule_start_date.strftime('%Y-%m-%d') + '  @ Pi:' + str(self.window.pi.mac_address)
#
#     class Meta:
#         unique_together = (('schedule_start_date', 'window'),)
#
#     def duplicate(self, new_start_date, new_end_date, new_window):
#         """
#         Duplicate the Schedule to a new date and/or time
#         :param new_start_date:
#         :param new_end_date:
#         :param new_window:
#         :return:
#         """
#
#
# class ScheduleItem(models.Model):
#     schedule = models.ForeignKey(Schedule, related_name='items')
#     video = models.ForeignKey('videos.Video')
#     video_start_seconds = models.PositiveIntegerField(null=True, blank=True)
#     video_duration_seconds = models.PositiveIntegerField(null=True, blank=True)
#     play_order = models.PositiveIntegerField()
#
#     class Meta:
#         unique_together = (('schedule', 'play_order'),)
#
#     def __str__(self):
#         return str(self.play_order) + ': ' + str(self.video)
