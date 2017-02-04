from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Avg

from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField
from taggit.managers import TaggableManager

from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField


class Video(models.Model):
    uploader_name = models.CharField(max_length=255, null=False, blank=True)
    address = models.CharField(max_length=255, null=False, blank=True)
    city = models.CharField(max_length=255, null=False, blank=True)
    state = USStateField(null=True, blank=True)
    zipcode = USZipCodeField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    file = models.FileField()
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    category = models.CharField(choices=[('D', 'Documentary'), ('N', 'Narrative'), ('A', 'Abstract'), ('An', 'Animation')], max_length=2, null=False, blank=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    status = models.CharField(choices=[('a', 'Approved'), ('r', 'Rejected'), ('s', 'Submitted')], max_length=1, default='s')
    moderated_by = models.ForeignKey('users.User', null=True, blank=True)
    moderation_notes = models.TextField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return ''.join(('Video: ', self.title, ' ', self.uploader_name))

    def get_absolute_url(self):
        return reverse('api:video-detail', kwargs={'pk': self.pk})

    @property
    def score_avg(self):
        """

        :return: Decimal of the Average Score for the Video
        """
        return self.videoscore_set.aggregate(Avg('score')).get('score__avg')


class VideoScore(models.Model):
    user = models.ForeignKey('users.User')
    video = models.ForeignKey('Video')
    score = models.IntegerField()

    def __str__(self):
        return 'User:' + str(self.user) + 'Video' + str(self.video)
