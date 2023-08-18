from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        respone = self.client.get('/')
        self.assertEqual(respone.status_code, 200)

    def test_about_page_status_code(self):
        respone = self.client.get('/about/')
        self.assertEqual(respone.status_code, 200)
