from django.db import models

from intellect_vault.models import Plot


class Beat(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
