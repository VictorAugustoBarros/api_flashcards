from django.shortcuts import render
from Card.models import Card
from Card.serializers import CardsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def CardList(request):
    card = Card.objects.all()
    serializer = CardsSerializer(card, many=True)
    return Response(serializer.data)
