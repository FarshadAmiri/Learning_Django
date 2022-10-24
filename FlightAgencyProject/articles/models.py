from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.contrib.admin import ModelAdmin
import re
import random


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article_page", kwargs={'slug' :self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
        super(Article, self).save(*args, **kwargs)