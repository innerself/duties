from decouple import config
from django.test import TestCase
from django.urls import reverse


class LoginPageTestCase(TestCase):
    def test_page_opens(self):
        response = self.client.get(reverse('duties:login'))
        self.assertEqual(response.status_code, 200)


class CalendarPageTestCase(TestCase):
    def test_page_opens(self):
        response = self.client.post(reverse('duties:login'), {
            'username': config('TEST_USER_LOGIN'),
            'password': config('TEST_USER_PASSWORD'),
        })
        self.assertEqual(response.status_code, 200)

        # TODO Test redirect

        response = self.client.get(reverse('duties:calendar'))
        self.assertEqual(response.status_code, 200)

    def test_anonymous_login_denied(self):
        pass
