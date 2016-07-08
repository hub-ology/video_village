from django.conf.urls import url
from django.views.generic import TemplateView

from .views import VideoCreate, overview

urlpatterns = [
    url(r'^add/$', VideoCreate.as_view(), name='videos-add'),
    url(r'^$', overview, name='list'),
    url(r'^moderation/$', TemplateView.as_view(template_name='videos/video_list.html'), name='moderation'),
    url(r'^success/$', TemplateView.as_view(template_name='videos/success.html'), name='success')
    ]