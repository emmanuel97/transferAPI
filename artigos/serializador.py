from rest_framework import serializers
from artigos.models import Artigo


class SerializadorArtigos(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = ('nome', 'conteudo')
