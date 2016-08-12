from django.shortcuts import render
from rest_framework import viewsets

from schedules.models import ScheduleItem, WindowShow
from schedules.serializers import ScheduleItemSerializer, WindowShowSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for videos.
    """
    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer


class WindowShowViewSet(viewsets.ModelViewSet):
    queryset = WindowShow.objects.all()
    serializer_class = WindowShowSerializer


    def get_queryset(self):
        show_date = self.request.query_params.get('show_date', None)
        window = self.request.query_params.get('window', None)

        queryset = WindowShow.objects.all()
        if show_date and window:
            show = ScheduleItem.objects.filter(date=show_date).values_list('show').first()[0]
            queryset = WindowShow.objects.filter(show=show, window__id=window)

        return queryset
