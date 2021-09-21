from django.db import models


class Card(models.Model):
    japanese = models.CharField(max_length=500)
    portuguese = models.CharField(max_length=500)
