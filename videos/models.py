from django.db import models
from django.core.urlresolvers import reverse


class Video(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()

    @property
    def video_length(self):
        return len(self.name)

    def __str__(self):
        return ''.join(('Video: ', self.name))

    def get_absolute_url(self):
        return reverse('api:video-detail', kwargs={'pk': self.pk})
