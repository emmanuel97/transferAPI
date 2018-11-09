from pontos_turisticos.models import Ponto_Turistico
from pontos_turisticos.serializador import SerializadorPontosTuristicos
from rest_framework import generics


class ListarPontosTuristicos(generics.ListCreateAPIView):
    queryset = Ponto_Turistico.objects.all()
    serializer_class = SerializadorPontosTuristicos


class DetalharPontosTuristicos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ponto_Turistico.objects.all()
    serializer_class = SerializadorPontosTuristicos
