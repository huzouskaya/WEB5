from django.test import TestCase

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import DiaryEntry

class DiaryEntryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_diary_entry(self):
        response = self.client.post('/diary/', {
            'title': 'Test Entry',
            'content': 'This is a test entry.'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_diary_entries(self):
        response = self.client.get('/diary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)