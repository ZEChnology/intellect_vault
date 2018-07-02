from django.db import models


class Deity(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    additional_domains = models.TextField()
