"""Card Views."""
from Card.models import Card
from Card.serializers import CardsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def CardList(request):
    """Método para listar todos os Cards cadastrados."""
    card = Card.objects.all()
    serializer = CardsSerializer(card, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def CardPost(request):
    """Método para cadastrar um novo Card."""
    serializer = CardsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def CardPut(request, pk):
    """Método para atualizar o Card do id *pk*."""
    card = Card.objects.get(id=pk)
    serializer = CardsSerializer(card, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def CardDelete(request, pk):
    """Método para deletar o Card do id *pk* cadastrado."""
    card = Card.objects.get(id=pk)
    card.delete()
    return Response("Apagado com sucesso!")


@api_view(["DELETE"])
def CardDeleteAll(request):
    """Método para deletar todos os Cards cadastrados."""
    cards = Card.objects.all()
    for card in cards:
        card.delete()

    return Response("Todos os Cards apagados com sucesso!")
