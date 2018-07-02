from django.db import models


class Plot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    themes = models.TextField()
