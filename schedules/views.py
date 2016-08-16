from django.shortcuts import render
from rest_framework import viewsets

from schedules.models import ScheduleItem
from schedules.serializers import ScheduleItemSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for videos.
    """
    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer
