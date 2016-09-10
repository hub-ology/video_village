from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route, authentication_classes, \
    detail_route
from rest_framework.response import Response

from video_village.authentication import PiAuthentication
from .models import Pi
from .serializers import PiSerializer


class PiViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Pi's
    """
    queryset = Pi.objects.all()
    serializer_class = PiSerializer
    authentication_classes = (PiAuthentication, )

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
        pi.status = data
        pi.save()

        return Response('OK')

