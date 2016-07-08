from django.shortcuts import render
from rest_framework import viewsets

from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for videos.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
