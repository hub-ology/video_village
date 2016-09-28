import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import list_route, authentication_classes, \
    detail_route
from rest_framework.response import Response

from schedules.models import Window
from video_village.authentication import PiAuthentication
from .models import Pi
from .serializers import PiSerializer


class PiViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Pi's
    """
    queryset = Pi.objects.all()
    serializer_class = PiSerializer
    authentication_classes = (PiAuthentication, SessionAuthentication, )

    @list_route(methods=['post'], )
    def register(self, request):
        user = PiAuthentication().authenticate(self.request)
        if user is None:
            return

        data = request.data

        pi, created = Pi.objects.get_or_create(mac_address=data['mac_address'])
        return_data = PiSerializer(pi).data
        return_data['new_pi'] = created
        return Response(return_data)

    @detail_route(methods=['post'], )
    def status(self, request, pk=None):
        pi = self.get_object()
        data = request.data
        if data:
            pi.status = json.dumps(data)
            pi.save()

        return Response('OK')

    @detail_route(methods=['post'],)
    def assign(self, request, pk=None):
        """
        Assign the Pi to a Window
        """
        pi = self.get_object()
        data = request.data

        window_number = data.get('window')

        if window_number:
            window = Window.objects.get(pk=window_number)
            window.pi = pi
            window.save()
        return Response('OK')

    @detail_route(methods=['post'], )
    def projector_on(self, request, pk=None):
        pi = self.get_object()
        return Response(pi.turn_projector_on())

    @detail_route(methods=['post'], )
    def projector_off(self, request, pk=None):
        pi = self.get_object()
        return Response(pi.turn_projector_off())

    @detail_route(methods=['get'],)
    def get_status(self, request, pk=None):
        pi = self.get_object()
        return Response(pi.get_status())

@login_required()
def projector_off(request, pk):
    pi = Pi.objects.get(pk=pk)
    return Response(pi.turn_projector_off())

@login_required()
def projector_on(request, pk):
    pi = Pi.objects.get(pk=pk)
    return Response(pi.turn_projector_on())
