from django.urls import path, include
from parserapp.models import Book, Comment, Author
from rest_framework import routers, serializers, viewsets
from parserapp.serializer import BookSerializer, CommentsSerializer, AuthorSerializer
from parserapp.permissions import ReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from userapp.models import UserAuthor


class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser|IsAuthenticated]
    queryset = Book.objects.prefetch_related('authors', 'comments').all()
    serializer_class = BookSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

