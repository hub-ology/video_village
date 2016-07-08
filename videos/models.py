from django.db import models
from django.core.urlresolvers import reverse


class Video(models.Model):
    uploader_name = models.CharField(max_length=255, null=False, blank=True)
    file = models.FileField()
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    status = models.CharField(choices=[('a', 'Approved'), ('r', 'Rejected'), ('s', 'Submitted')], max_length=1, default='s')
    moderated_by = models.ForeignKey('users.User', null=True, blank=True)
    moderation_notes = models.TextField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return ''.join(('Video: ', self.title, ' ', self.uploader_name))

    def get_absolute_url(self):
        return reverse('api:video-detail', kwargs={'pk': self.pk})
