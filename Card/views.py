"""Card Views."""
from Card.models import Card
from Card.serializers import CardsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def CardList(request):
    """Método para listar todos os Cards cadastrados."""
    try:
        card = Card.objects.all()
        serializer = CardsSerializer(card, many=True)
        return Response(serializer.data)

    except Exception as err:
        return Response("Erro ao buscar Cards: %s" % err, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def CardPost(request):
    """Método para cadastrar um novo Card."""
    try:
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as err:
        return Response("Falha ao cadastrar Card: %s" % request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def CardPut(request, pk):
    """Método para atualizar o Card do id *pk*."""
    try:
        card = Card.objects.get(id=pk)
        serializer = CardsSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as err:
        return Response("Falha ao atualizar Card: %s" % request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def CardDelete(request, pk):
    """Método para deletar o Card do id *pk* cadastrado."""
    try:
        card = Card.objects.get(id=pk)
        card.delete()
        return Response("Apagado com sucesso!")

    except Exception as err:
        return Response("Falha ao deletar Card: %s" % request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def CardDeleteAll(request):
    """Método para deletar todos os Cards cadastrados."""
    try:
        cards = Card.objects.all()
        for card in cards:
            card.delete()

        return Response("Todos os Cards apagados com sucesso!")

    except Exception as err:
        return Response("Falha ao deletar todos os Cards: %s" % err, status=status.HTTP_400_BAD_REQUEST)
