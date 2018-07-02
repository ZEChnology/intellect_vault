from django.db import models

from intellect_vault.models import World


class Region(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    world = models.ForeignKey(World, on_delete=models.CASCADE)
