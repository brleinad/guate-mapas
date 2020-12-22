from django.urls import reverse
from rest_framework import status

from .base_test import BaseTest

class UsersTests(BaseTest):

    center_geolocation = {
        'type': 'Point',
        'coordinates': [0, 0]
    }

    def __init__(self, *args, **kwargs):
        url = self.api_url + reverse('geolocations-list')
        super().__init__(*args, **kwargs)

    def test_cannot_create_geolocation_if_not_logged_ind(self):
        self.client.logout()
        response = self.client.post(self.url, self.center_geolocation)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_geolocations(self):
        response = self.client.post(self.url, self.center_geolocation)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.center_geolocation)

        response = self.client.get(self.url, self.center_geolocation)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [self.center_geolocation])
