from rest_framework import serializers
from posts.models import Post
from books.models import Book

class PostSerializer(serializers.ModelSerializer):
    class Meta:
                fields = ('id', 'title', 'author', 'discription', 'create_at', 'update_at',)
                model = Post

class BookSerializer(serializers.ModelSerializer):
    class Meta:
                fields = ('id', 'title', 'author', 'discription', 
                'create_at', 'update_at',)
                model = Book
