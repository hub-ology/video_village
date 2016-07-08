from django.test import TestCase
from model_mommy import mommy

from .models import Video


class VideoModelTest(TestCase):

    def setUp(self):
        self.video = mommy.make(Video)

    def test_create(self):
        self.assertTrue(isinstance(self.video, Video))

    def test_str(self):
        self.assertEqual(''.join(('Video: ', self.video.title, ' ', self.video.uploader_name)), str(self.video))

