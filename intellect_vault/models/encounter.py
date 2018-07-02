from django.db import models

from intellect_vault.models import District, Wilds


class Encounter(models.Model):
    name = models.CharField(max_length=150)
    SCRIPTED = 'SCR'
    RANDOM = 'RND'
    NATURE_CHOICES = (
        (SCRIPTED, 'Scripted'),
        (RANDOM, 'Random')
    )
    nature = models.CharField(
        max_length=3,
        choices=NATURE_CHOICES,
        default=SCRIPTED
    )
    description = models.TextField()
    sequence = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    wilds = models.ForeignKey(Wilds, on_delete=models.CASCADE)
