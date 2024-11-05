from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """create a blog model"""

    class Meta:
        ordering = ("id",)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """create a blog model"""

    class Meta:
        ordering = ("created_at",)

    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
