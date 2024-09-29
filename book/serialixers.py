from rest_framework import serializers
from .models import Snippet
from .models import Author
from .models import Book
from .models import Category

class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'