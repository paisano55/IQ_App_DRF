from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,Quote
from .serializers import CpuSerializer,MbSerializer,RamSerializer,VgaSerializer,SsdSerializer,HddSerializer,CaseSerializer,PsuSerializer

class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(content, **kwargs)

@csrf_exempt
def cpu_list(request):
    if request.method == 'GET':
        queryset = CPU.objects.all()
        serializer = CpuSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CpuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def mb_list(request):
    queryset = MB.objects.all()
    serializer = MbSerializer(queryset, many=True)
    return JsonResponse(serializer.data)

def ram_list(request):
    queryset = RAM.objects.all()
    serializer = RamSerializer(queryset, many=True)
    return JsonResponse(serializer.data)

def vga_list(request):
    queryset = VGA.objects.all()
    serializer = VgaSerializer(queryset, many=True)  
    return JsonResponse(serializer.data)

def ssd_list(request):
    queryset = SSD.objects.all()
    serializer = SsdSerializer(queryset, many=True)
    return JsonResponse(serializer.data)

def hdd_list(request):
    queryset = HDD.objects.all()
    serializer = HddSerializer(queryset, many=True)
    return JsonResponse(serializer.data)

def case_list(request):
    queryset = CASE.objects.all()
    serializer = CaseSerializer(queryset, many=True)
    return JsonResponse(serializer.data)

def psu_list(request):
    queryset = PSU.objects.all()
    serializer = PsuSerializer(queryset, many=True)
    return JsonResponse(serializer.data)