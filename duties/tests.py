from decouple import config
from django.test import TestCase
from django.urls import reverse


class LoginPageTestCase(TestCase):
    def test_page_opens(self):
        response = self.client.get(reverse('duties:login'))
        self.assertEqual(response.status_code, 200)


class CalendarPageTestCase(TestCase):
    user_auth_data = {
        'username': config('TEST_USER_LOGIN'),
        'password': config('TEST_USER_PASSWORD'),
    }

    def test_page_opens(self):
        self.client.post(reverse('duties:login'), self.user_auth_data)
        response = self.client.get(reverse('duties:calendar'))
        # TODO Will it always redirect despite of user is authenticated?
        #  Is this because of @login_required?
        self.assertEqual(response.status_code, 302)

    def test_anonymous_login_denied(self):
        response = self.client.get(reverse('duties:calendar'), follow=True)
        self.assertRedirects(
            response,
            f"{reverse('duties:login')}?next={reverse('duties:calendar')}",
            status_code=302,
            target_status_code=200,
        )
