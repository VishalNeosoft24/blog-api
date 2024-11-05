from django.contrib import admin

from .models import Blog, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """CategoryAdmin"""

    list_display = [
        "id",
        "name",
        "description",
    ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """BlogAdmin"""

    list_display = ["id", "author", "category", "title", "content"]
