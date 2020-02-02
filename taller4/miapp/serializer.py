from rest_framework import serializers
from .models import *

# class ToolInputSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ToolInput
#         fields = '__all__'
#
# class ToolSerializer(serializers.HyperlinkedModelSerializer):
#     #inputs = ToolInputSerializer(many=True)
#
#     class Meta:
#         model = Tool
#         fields = ('label', 'description')

class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ('nombre','precio','año')
