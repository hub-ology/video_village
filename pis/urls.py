from django.conf.urls import url

from pis.views import projector_off, projector_on

urlpatterns = [
    url(r'^pi/(?P<pk>[\d]+)/projector/off$', projector_off, name='projector_off'),
    url(r'^pi/(?P<pk>[\d]+)/projector/on$', projector_on, name='projector_on'),
]
