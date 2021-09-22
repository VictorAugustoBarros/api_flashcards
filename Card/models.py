"""Card Model."""
from django.db import models


class Card(models.Model):
    """Class Model Card."""

    japanese = models.CharField(max_length=500)
    portuguese = models.CharField(max_length=500)
