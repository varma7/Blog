from django.db import models

class BlogModel(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    text = models.TextField()
