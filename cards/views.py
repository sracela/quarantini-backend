from django.http import HttpResponse
from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
