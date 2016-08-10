from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.template import Context
from django.views.generic import FormView, CreateView
from rest_framework import viewsets, generics

from .models import Video
from .serializer import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for videos.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoCreate(CreateView):
    model = Video
    fields = ['uploader_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'title', 'description',
              'category', 'file']
    success_url = reverse_lazy('videos:success')


def overview(request):

    mod_queue = Video.objects.filter(approved=False)


    t = 'videos/overview.html'
    c = {
        'moderation_queue_count': len(mod_queue),
        'total_videos': Video.objects.count(),
        'awaiting_moderation': mod_queue,
    }

    return render(request, t, c)
