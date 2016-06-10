from django.conf.urls import url
from django.views.generic import TemplateView

from .views import VideoCreate

urlpatterns = [
    url(r'^add/$', VideoCreate.as_view(), name='videos-add'),
    url(r'^$', TemplateView.as_view(template_name='videos/video_list.html'))
    ]