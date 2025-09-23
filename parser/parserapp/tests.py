from django.test import TestCase
from faker import Faker
from userapp.models import UserAuthor
from .models import Book, Author, Comment
from mixer.backend.django import mixer
# Create your tests here.
class BookTestCaser(TestCase):
    def setUp(self):
        faker = Faker()
        author = Author.objects.create(name=faker.name())
        user = UserAuthor.objects.create(username=faker.name(), email=faker.email(),
                                         password=faker.password())
        self.comment = Comment.objects.create(name=user, comment=faker.name())
        self.book = Book.objects.create(title=faker.name(),
                                        content= faker.name(),
                                        href='http//:test_href.ru',
                                        user=user
                                        )
        self.book.authors.add(author)
    def test_has_img_false(self):
        self.assertFalse(self.book.is_img())
    def test_has_img_true(self):
        self.book.img_href = 'media/test.jpg'
        self.assertTrue(self.book.is_img())
    def test_count_comments(self):
        self.book.comments.add(self.comment)
        self.assertEqual(self.book.count_comments(), 1)

class BookTestCaserMixer(TestCase):
    def setUp(self):
        self.comment = mixer.blend(Comment)
        self.book = mixer.blend(Book)
    def test_has_img_false(self):
        self.assertFalse(self.book.is_img())
    def test_has_img_true(self):
        self.book.img_href = 'media/test.jpg'
        self.assertTrue(self.book.is_img())
    def test_count_comments(self):
        self.assertEqual(self.book.count_comments(), 0)
        self.book.comments.add(self.comment)
        self.assertEqual(self.book.count_comments(), 1)

