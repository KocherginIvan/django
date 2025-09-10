from django.db import models
from userapp.models import UserAuthor
# Create your models here.

class NameStamp(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Author(NameStamp):
    def __str__(self):
        return self.name

class Comment(NameStamp, models.Model):
    comment = models.TextField()
    def __str__(self):
        return self.name, self.comment

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books_author')
    content = models.TextField()
    href = models.URLField()
    img_href = models.ImageField(upload_to='books', null=True, blank=True)
    comments = models.ManyToManyField(Comment)
    user = models.ForeignKey(UserAuthor, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def is_img(self):
        return bool(self.img_href)
    def get_comments(self):
        return self.comments.all()

    def count_comments(self):
        return self.comments.count()

