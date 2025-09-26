from django.urls import path, include
from userapp.models import UserAuthor

from .models import Book, Comment, Author
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.

class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True,
        read_only=True,
        view_name='comment-detail'
                                                   )
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = ['url', 'title', 'authors', 'content', 'comments']
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name']
class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'name', 'comment']
