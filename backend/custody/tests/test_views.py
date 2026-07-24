from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_events(self):
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, 200)
