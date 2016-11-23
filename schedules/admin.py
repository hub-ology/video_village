from django.contrib import admin

# from schedules.models import ScheduleItem, Schedule
#
# admin.site.register(Schedule)
# admin.site.register(ScheduleItem)


################################################################################
#
# Refer to https://docs.djangoproject.com/en/1.8/intro/tutorial02/
#


from schedules.models import Window, Playlist, VideoSegment, Show, WindowShow, ScheduleItem



class ScheduleItemInline(admin.TabularInline):
    model = ScheduleItem
    extra = 0


class ShowAdmin(admin.ModelAdmin):
    inlines = [
        ScheduleItemInline,
    ]


class VideoSegmentInline(admin.TabularInline):
    model = VideoSegment
    # ...
    list_display = ('video', 'offset_in_playlist', 'offset_in_video', 'duration', 'playlist')
    list_filter = ['playlist']

class PlaylistAdmin(admin.ModelAdmin):
    model = Playlist
    extra = 0
    inlines = [VideoSegmentInline,]


class ScheduleItemAdmin(admin.ModelAdmin):
    model = ScheduleItem
    save_as = True



# admin.site.register(Window)  # Registered in video_village/pis
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(VideoSegment)
admin.site.register(Show, ShowAdmin)
admin.site.register(WindowShow)
admin.site.register(ScheduleItem, ScheduleItemAdmin)
