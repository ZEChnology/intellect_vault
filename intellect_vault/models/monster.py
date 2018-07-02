from django.db import models

from intellect_vault.models import Encounter, Faction


class Monster(models.Model):
    name = models.CharField(max_length=150)
    appearance = models.TextField()
    voice = models.TextField()
    LAWFUL_GOOD = 'LG'
    NEUTRAL_GOOD = 'NG'
    CHAOTIC_GOOD = 'CG'
    LAWFUL_NEUTRAL = 'LN'
    TRUE_NUETRAL = 'NN'
    CHAOTIC_NUETRAL = 'CN'
    LAWFUL_EVIL = 'LE'
    NEUTRAL_EVIL = 'NE'
    CHAOTIC_EVIL = 'CE'
    ALIGNMENT_CHOICES = (
        (LAWFUL_GOOD, 'Lawful Good'),
        (NEUTRAL_GOOD, 'Neutral Good'),
        (CHAOTIC_GOOD, 'Chaotic Good'),
        (LAWFUL_NEUTRAL, 'Lawful Neutral'),
        (TRUE_NUETRAL, 'True Neutral'),
        (CHAOTIC_NUETRAL, 'Chaotic Neutral'),
        (LAWFUL_EVIL, 'Lawful Evil'),
        (NEUTRAL_EVIL, 'Neutral Evil'),
        (CHAOTIC_EVIL, 'Chaotic Evil'),
    )
    alignment = models.CharField(
        max_length=2,
        choices=ALIGNMENT_CHOICES,
        default=TRUE_NUETRAL,
    )
    factions = models.ManyToManyField(Faction)
    encounters = models.ManyToManyField(Encounter)
