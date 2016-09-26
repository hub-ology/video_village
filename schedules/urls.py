from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WindowList, WindowDetail, all_windows_projector_on, all_windows_projector_off, ShowList, ShowDetail

urlpatterns = [
    url(r'^$', login_required(WindowList.as_view()), name='list'),
    url(r'^shows$', login_required(ShowList.as_view()), name='show_list'),

    url(r'^all_on$', all_windows_projector_on, name='all_on'),
    url(r'^all_off$', all_windows_projector_off, name='all_off'),

    url(r'^(?P<pk>[\d]+)$', login_required(WindowDetail.as_view()), name='detail'),
    url(r'^shows/(?P<pk>[\d]+)$', login_required(ShowDetail.as_view()), name='show_detail'),
    ]
