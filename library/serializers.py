from rest_framework import serializers
from .models import Book, Author, Editorial

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    editorial = serializers.StringRelatedField()

    class Meta:
        model=Book
        fields = ('code', 'book', 'author', 'editorial', 'thumbnail', 'slug', 'genre', 'published')