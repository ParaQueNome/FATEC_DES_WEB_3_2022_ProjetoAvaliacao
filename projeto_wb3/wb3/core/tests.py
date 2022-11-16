from django.test import TestCase
from http import HTTPStatus

# Create your tests here.
class SemPalestra(TestCase):
    def test_200_response(self):
        if resp.status == HTTPStatus.Ok:
            self.assertEqual('Ok', self.resp.status_code)