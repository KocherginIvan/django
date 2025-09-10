from django.test import Client, TestCase
from faker import Faker
from userapp.models import UserAuthor
from .models import Book, Author, Comment
from mixer.backend.django import mixer

class OpenTestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = mixer.blend(Book, img_href='media/1.jpg')
        self.faker = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/work/1')
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        user = UserAuthor.objects.create_user(username='test_user', email='test@test.com', password='sad5456331')
        response = self.client.get('/comment/1')
        self.assertEqual(response.status_code, 302)
        self.client.login(username='test_user', password='sad5456331')
        response = self.client.get('/comment/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/comment/1',
                                    {'name': user, 'comment': self.faker.text()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.book.count_comments(), 1)