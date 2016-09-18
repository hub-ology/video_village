from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WindowList

urlpatterns = [
    url(r'^$', login_required(WindowList.as_view()), name='list'),
    ]
