from django.test import TestCase
from django.test import Client
from django.urls import reverse


class AboutViewTest(TestCase):

    def test_about_view(self):
        c = Client()
        url = reverse('page-about')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)


class PageViewTest(TestCase):

    def test_page_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

