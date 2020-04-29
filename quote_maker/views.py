from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,Quote
from .serializers import CpuSerializer,MbSerializer,RamSerializer,VgaSerializer,SsdSerializer,HddSerializer,CaseSerializer,PsuSerializer


class CpuViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CpuSerializer