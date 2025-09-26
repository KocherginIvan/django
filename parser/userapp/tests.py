from django.test import TestCase
import requests

class BookTestCaser(TestCase):
    def test_api_without_avtorization(self):
        response = requests.get("http://127.0.0.1:8000/api/v0/books/")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'detail': 'Учетные данные не были предоставлены.'})
    def test_api_with_avtorization(self):
        token = '2f7d4a16e683d1624b1675da706b46e970e046ac'
        print(token)
        headers = {'Authorization': 'Token ' + token}
        response = requests.get("http://127.0.0.1:8000/api/v0/books/", headers=headers)
        self.assertEqual(response.status_code, 200)
