from Card.models import Card
from rest_framework import serializers


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["japanese", "portuguese"]
