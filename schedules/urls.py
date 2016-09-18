from django.conf.urls import url

from .views import WindowList

urlpatterns = [
    url(r'^$', WindowList.as_view(), name='list'),
    ]
