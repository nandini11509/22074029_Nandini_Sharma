from django.db import models

# Create your models here.
class UrlShortener(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)