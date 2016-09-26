from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WindowList, WindowDetail, all_windows_projector_on, all_windows_projector_off

urlpatterns = [
    url(r'^$', login_required(WindowList.as_view()), name='list'),
    url(r'^all_on$', all_windows_projector_on, name='all_on'),
    url(r'^all_off$', all_windows_projector_off, name='all_off'),

    url(r'^(?P<pk>[\d]+)$', login_required(WindowDetail.as_view()), name='detail'),
    ]
