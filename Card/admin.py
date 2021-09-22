"""Card Admin."""
from django.contrib import admin
from Card import models

admin.site.register(models.Card)
