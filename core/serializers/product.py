from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from ..models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer, StringRelatedField

# from projeto.models import Avaliacao, Equipe

# class EquipeDetalheSerializer(ModelSerializer):
#     class Meta:
#         model = Equipe
#         fields = "__all__"
#         depth = 1

# class AvaliacaoReadSerializer(ModelSerializer):
#     Equipe = EquipeDetalheSerializer()

#     class Meta:
#         model = Avaliacao
#         fields = "__all__"
#         depth = 1
       
# class AvaliacaoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Avaliacao
#         fields = "__all__"
#         depth = 1