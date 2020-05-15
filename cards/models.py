from django.db import models


class Card(models.Model):
    description = models.TextField()
    image_url = models.URLField()
