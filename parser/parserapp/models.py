from django.db import models
from userapp.models import UserAuthor
class NameStamp(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True
# Create your models here.
class Author(NameStamp):
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    name = models.ForeignKey(UserAuthor, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name, self.comment

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    content = models.TextField()
    href = models.URLField()
    img_href = models.ImageField(upload_to='books', null=True, blank=True)
    comments = models.ManyToManyField(Comment)
    user = models.ForeignKey(UserAuthor, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

