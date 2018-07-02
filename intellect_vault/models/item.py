from django.db import models

from intellect_vault.models import NPC, Monster


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    rules = models.TextField()
    value = models.TextField()
    npcs = models.ManyToManyField(NPC)
    monsters = models.ManyToManyField(Monster)
