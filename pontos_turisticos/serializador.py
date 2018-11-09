from rest_framework import serializers
from pontos_turisticos.models import Ponto_Turistico


class SerializadorPontosTuristicos(serializers.ModelSerializer):
    class Meta:
        model = Ponto_Turistico
        fields = ('nome', 'cidade', 'descricao','image','rank')
