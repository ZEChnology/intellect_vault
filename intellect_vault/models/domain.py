from django.db import models

from intellect_vault.models import Deity


class Domain(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    deities = models.ManyToManyField(Deity)
