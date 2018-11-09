from praias.models import Praia
from praias.serializador import SerializadorPraias
from rest_framework import generics


class ListarPraias(generics.ListCreateAPIView):
    queryset = Praia.objects.all()
    serializer_class = SerializadorPraias


class DetalharPraias(generics.RetrieveUpdateDestroyAPIView):
    queryset = Praia.objects.all()
    serializer_class = SerializadorPraias
