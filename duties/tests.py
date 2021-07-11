from django.test import TestCase
from django.urls import reverse


class LoginTestCase(TestCase):
    def test_page_opens(self):
        response = self.client.get(reverse('duties:login'))
        self.assertEqual(response.status_code, 200)
