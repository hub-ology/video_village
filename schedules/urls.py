from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WindowList, WindowDetail

urlpatterns = [
    url(r'^$', login_required(WindowList.as_view()), name='list'),
    url(r'^(?P<pk>[\d]+)$', login_required(WindowDetail.as_view()), name='detail'),
    ]
