from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class BaseTest(APITestCase):

    api_url = 'http://testserver'
    url = api_url + reverse('user-list')
    user_lolis = {
        'first_name': 'Lolis',
        'last_name': 'Polis',
        'username': 'lolis',
        'email': 'lolis@polis.ca',
        'password': 'password'
    }
    user_admin = {
        'username': 'admin',
        'email': 'admin@test.com',
        'password': 'adminsecret'
    }

    def setUp(self):
        self.user = User.objects.create_user(self.user_admin.get('username'), email=self.user_admin.get('email'), password=self.user_admin.get('password'))
        login = self.client.login(username=self.user_admin.get('username'), password=self.user_admin.get('password'))
