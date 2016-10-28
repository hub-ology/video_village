from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from videos.serializer import VideoSerializer
from .models import ScheduleItem, WindowShow, Playlist, VideoSegment, Show

class ScheduleItemSerializer(serializers.ModelSerializer):
    # video = VideoSerializer()
    show = serializers.StringRelatedField()

    class Meta:
        model = ScheduleItem
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):
    scheduleitem_set = ScheduleItemSerializer(many=True)

    class Meta:
        model = Show
        fields = ('scheduleitem_set',)


class VideoSegmentSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    class Meta:
        model = VideoSegment
        fields = ('video', 'offset_in_playlist', 'offset_in_video', 'duration',)


class PlaylistSerializer(serializers.ModelSerializer):
    videosegment_set = VideoSegmentSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('title', 'notes', 'videosegment_set')


class WindowShowSerializer(serializers.ModelSerializer):
    show = SerializerMethodField()
    playlist = PlaylistSerializer()

    class Meta:
        model = WindowShow
        fields = '__all__'

    def get_show(self, obj):
        # return {'test': 'test'}
        dte = self.context.get('date', None)
        if dte:
            si = ScheduleItem.objects.filter(date=dte)
        else:
            si = ScheduleItem.objects.all()
        serializer = ScheduleItemSerializer(si, many=True)
        data = {'scheduleitem_set': serializer.data}

        return data


# class ScheduleSerializer(serializers.ModelSerializer):
#     items = ScheduleItemSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Schedule
#         fields = ('schedule_start_date', 'schedule_end_date', 'window', 'items')
