from django.shortcuts import render

from rest_framework import viewsets
from .models import product_details
from .serializers import product_serializer




class products(viewsets.ModelViewSet):
    queryset = product_details.objects.all()
    serializer_class = product_serializer

