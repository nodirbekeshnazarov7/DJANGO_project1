from django.db import models
from django.views.generic import TemplateView
# Create your models here.

class PostHomeCarousel(models.Model):
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    button = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.theme