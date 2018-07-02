from django.db import models

from intellect_vault.models import Region


class Wilds(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
