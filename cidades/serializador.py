from rest_framework import serializers
from cidades.models import Cidade


class SerializadorCidades(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('nome', 'descricao','image','rank')
