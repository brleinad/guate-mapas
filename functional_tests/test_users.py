from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from .base_test import BaseTest

class UsersTests(BaseTest):

    user_lolis = {
        'first_name': 'Lolis',
        'last_name': 'Polis',
        'username': 'lolis',
        'email': 'lolis@polis.ca',
        'password': 'password'
    }

    def __init__(self, *args, **kwargs):
        url = self.api_url + reverse('user-list')
        super().__init__(*args, **kwargs)

    def test_cannot_create_user_if_not_logged_in(self):
        self.client.logout()
        response = self.client.post(self.url, self.user_lolis)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_account(self):
        response = self.client.post(self.url, self.user_lolis)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'url': f'{self.url}2/',
            'email': self.user_lolis.get('email'),
            'username': self.user_lolis.get('username'),
            'first_name': self.user_lolis.get('first_name'),
            'last_name': self.user_lolis.get('last_name'),
            'password': self.user_lolis.get('password'),
            'groups': []
        })

        response = self.client.get(self.url)
        test_users = [self.user_lolis]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
