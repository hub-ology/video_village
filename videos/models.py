from django.db import models
from django.core.urlresolvers import reverse


class Video(models.Model):
    uploader_name = models.CharField(max_length=255, null=False, blank=True)
    file = models.FileField()
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)

    @property
    def video_length(self):
        return len(self.title)

    def __str__(self):
        return ''.join(('Video: ', self.title, ' ', self.uploader_name))

    def get_absolute_url(self):
        return reverse('api:video-detail', kwargs={'pk': self.pk})
