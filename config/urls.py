# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.views import defaults as default_views
from rest_framework import routers

from pis.views import PiViewSet
from schedules.views import ScheduleViewSet, WindowShowViewSet
from videos.views import VideoViewSet

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register('schedules', ScheduleViewSet)
router.register('pis', PiViewSet)
router.register('windows', WindowShowViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/callforsubmission.html'), name='home'),
    # url(r'^$', RedirectView.as_view(url=reverse_lazy('videos:videos-add')), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('video_village.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),


    # Your stuff: custom urls includes go here
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^videos/', include('videos.urls', namespace='videos')),

    url(r'windows/', include('schedules.urls', namespace='windows')),
    url(r'pis/', include('pis.urls', namespace='pis')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
