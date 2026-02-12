from django.test import TestCase


class TrackerSmokeTest(TestCase):
    def test_root(self):
        resp = self.client.get('/')
        self.assertIn(resp.status_code, (200, 301, 302))
