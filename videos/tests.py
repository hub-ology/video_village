from django.test import TestCase
from model_mommy import mommy

from .models import Video, VideoScore


class VideoModelTest(TestCase):

    def setUp(self):
        self.video = mommy.make(Video)

    def test_create(self):
        self.assertTrue(isinstance(self.video, Video))

    def test_str(self):
        self.assertEqual(''.join(('Video: ', self.video.title, ' ', self.video.uploader_name)), str(self.video))

    def test_avg_score(self):
        self.assertIsNone(self.video.score_avg)

        self.video_score = mommy.make(VideoScore)
        self.assertEqual(self.video_score.score, self.video_score.video.score_avg)

        self.video_score2 = mommy.make(VideoScore, video=self.video_score.video)
        score2 = (self.video_score.score + self.video_score2.score) / 2
        self.assertEqual(score2, self.video_score.video.score_avg)

