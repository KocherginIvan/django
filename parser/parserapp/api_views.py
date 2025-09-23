from django.urls import path, include
from parserapp.models import Book, Comment, Author
from rest_framework import routers, serializers, viewsets
from parserapp.serializer import BookSerializer, CommentsSerializer, AuthorSerializer
from rest_framework.decorators import action

from userapp.models import UserAuthor


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
