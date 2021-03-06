from django.db import models
from django.urls import reverse

import uuid


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True, default=uuid.uuid1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[self.slug])


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='notes')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    slug = models.SlugField(max_length=50, unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Note-update', args=[self.slug])
