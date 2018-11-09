from rest_framework import serializers
from praias.models import Praia


class SerializadorPraias(serializers.ModelSerializer):
    class Meta:
        model = Praia
        fields = ('nome', 'cidade', 'endereco', 'descricao','image','rank')
