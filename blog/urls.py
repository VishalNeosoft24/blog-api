from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.CategoryView.as_view(), name="category"),
    path("blog/", views.BlogView.as_view(), name="blog"),
]
