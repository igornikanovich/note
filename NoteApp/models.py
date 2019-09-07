from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[self.slug])


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.title
