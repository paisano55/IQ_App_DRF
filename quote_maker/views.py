from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,Quote
from .serializers import CpuSerializer,MbSerializer,RamSerializer,VgaSerializer,SsdSerializer,HddSerializer,CaseSerializer,PsuSerializer


def cpu_list(request):
    cpu = CPU.objects.all()
    serialzer = CpuSerializer(cpu, many=True)
    json_data = JSONRenderer().render(serialzer.data)

    return HttpResponse(json_data)