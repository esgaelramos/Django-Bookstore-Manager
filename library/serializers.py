from rest_framework import serializers
from .models import Book, Author, Editorial

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ('code', 'book', 'author', 'editorial', 'thumbnail', 'slug', 'genre', 'published')