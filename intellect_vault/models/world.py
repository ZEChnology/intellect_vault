from django.db import models


class World(models.Model):
    name=models.CharField(limit=150)
    description=models.TextField()
