from django.db import models

from intellect_vault.models import Nation


class City(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
