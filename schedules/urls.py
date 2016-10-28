from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WindowList, WindowDetail, all_windows_projector_on, all_windows_projector_off, ShowList, ShowDetail, \
    all_windows_sync, all_windows_cache_clear, all_windows_stream

urlpatterns = [
    url(r'^$', login_required(WindowList.as_view()), name='list'),
    url(r'^shows$', login_required(ShowList.as_view()), name='show_list'),

    url(r'^all_on$', all_windows_projector_on, name='all_on'),
    url(r'^all_off$', all_windows_projector_off, name='all_off'),
    url(r'^all_cache_clear$', all_windows_cache_clear, name='all_cache_clear'),
    url(r'^all_sync$', all_windows_sync, name='all_sync'),

    url(r'^(?P<pk>[\d]+)$', login_required(WindowDetail.as_view()), name='detail'),
    url(r'^shows/(?P<pk>[\d]+)$', login_required(ShowDetail.as_view()), name='show_detail'),


    url(r'^stream$', all_windows_stream, name='stream_form'),


    ]
