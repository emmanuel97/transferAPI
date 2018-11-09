from artigos.models import Artigo
from artigos.serializador import SerializadorArtigos
from rest_framework import generics


class ListarArtigos(generics.ListCreateAPIView):
    queryset = Artigo.objects.all()
    serializer_class = SerializadorArtigos


class DetalharArtigos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artigo.objects.all()
    serializer_class = SerializadorArtigos
