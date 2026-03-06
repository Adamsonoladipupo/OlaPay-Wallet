from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user import url
from .models import User
# Create your tests here.

class TestSignUp(TestCase):
    #arrange
    #act
    #assert

    def test_signup(self):

        def test_signup_return_201(self):
            url = reverse('register')
            data = {
                "first_name": "Blessing",
                "last_name": "Udo",
                "username": "blessing_udo",
                "email": "blessing.udo@yahoo.com",
                "phone": "08155664433",
                "password": "Password123!"
            }
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_with_an_invalid_email_return_404(self):
        url = reverse('register')
        data = {
            "first_name": "Blessing",
            "last_name": "Udo",
            "username": "blessing_udo",
            "email": "blessing",
            "phone": "08155664433",
            "password": "Password123!"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)