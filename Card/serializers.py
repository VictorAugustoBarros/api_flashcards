"""Serializer Modules."""
from Card.models import Card
from rest_framework import serializers


class CardsSerializer(serializers.ModelSerializer):
    """Classe Serializer da model Card."""

    class Meta:
        """Classe modelo Card."""

        model = Card
        fields = ["japanese", "portuguese"]
