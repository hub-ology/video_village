from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.template import Context
from django.views.generic import FormView, CreateView
from django.views.generic.edit import ModelFormMixin
from rest_framework import viewsets, generics

from videos.forms import VideoForm
from videos.tables import SimpleTable
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
    form_class = VideoForm
    success_url = reverse_lazy('videos:success')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        for f in self.request.FILES.getlist('file'):
            self.object.pk = None
            self.object.file = f
            self.object.save()

        return super(VideoCreate, self).form_valid(form)


@login_required
def overview(request):

    mod_queue = Video.objects.filter(approved=False)


    t = 'videos/overview.html'
    c = {
        'moderation_queue_count': len(mod_queue),
        'total_videos': Video.objects.count(),
        'video_table': SimpleTable(Video.objects.all()),
        'awaiting_moderation': mod_queue,
    }

    return render(request, t, c)


@login_required
def moderate(request):

    video_list = Video.objects.all()

    t = 'videos/moderate.html'
    c = {'video_list': video_list}
    return render(request, t, c)
