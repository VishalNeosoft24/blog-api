from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    """CategorySerializer"""

    class Meta:
        model = Category
        fields = ["name", "description"]


class BlogSerializer(serializers.ModelSerializer):
    """BlogSerializer"""

    class Meta:
        model = Blog
        fields = [
            "author",
            "category",
            "title",
            "content",
        ]
