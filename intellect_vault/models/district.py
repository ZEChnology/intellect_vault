from django.db import models

from intellect_vault.models import City


class District(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
