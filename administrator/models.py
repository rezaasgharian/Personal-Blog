from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='PostImages')
    publish = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()