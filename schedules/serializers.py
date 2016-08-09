from rest_framework import serializers

from videos.serializer import VideoSerializer
from .models import Schedule, ScheduleItem


class ScheduleItemSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = ScheduleItem
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    items = ScheduleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ('schedule_start_date', 'schedule_end_date', 'window', 'items')
