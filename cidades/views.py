from cidades.models import Cidade
from cidades.serializador import SerializadorCidades
from rest_framework import generics


class ListarCidades(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = SerializadorCidades


class DetalharCidades(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = SerializadorCidades
