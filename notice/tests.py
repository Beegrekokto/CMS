from django.test import TestCase
from django.test import Client


class ContactViewTest(TestCase):

    def test_page_detail_view(self):
        c = Client()
        response = c.get('/notice/')
        self.assertEqual(response.status_code, 200)