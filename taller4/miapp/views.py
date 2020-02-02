from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import *
from .serializer import CarroSerializer

import requests

# Create your views here.
class CarrosViewSet(generics.ListCreateAPIView):
    '''
    Contiene información sobre carros
    '''
    queryset = Carro.objects.all()
    #lookup_field = 'id'
    serializer_class = CarroSerializer

class CarroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


