from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from rest_framework import viewsets

from schedules.models import ScheduleItem, WindowShow, Window
from schedules.serializers import ScheduleItemSerializer, WindowShowSerializer
from video_village.authentication import PiAuthentication


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for videos.
    """
    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer


class WindowShowViewSet(viewsets.ModelViewSet):
    queryset = WindowShow.objects.all()
    serializer_class = WindowShowSerializer
    authentication_classes = (PiAuthentication,)


    def get_queryset(self):
        show_date = self.request.query_params.get('show_date', None)
        window = self.request.query_params.get('window', None)
        mac_address = self.request.query_params.get('mac', None)

        queryset = WindowShow.objects.all()
        if show_date:
            show_items = ScheduleItem.objects.filter(date=show_date).values_list('show').first()
            if show_items:
                show = show_items[0]
            else:
                show = None
            queryset = queryset.filter(show=show)

        if window:
            queryset = queryset.filter(window__id=window)

        if mac_address:
            queryset = queryset.filter(window__pi__mac_address=mac_address)

        return queryset


class WindowList(ListView):
    model = Window
    ordering = 'pk'


class WindowDetail(DetailView):
    model = Window
