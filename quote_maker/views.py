from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .quotemaker import QuoteMaker

from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,QUOTE
from .serializers import CpuSerializer,MbSerializer,RamSerializer,VgaSerializer,SsdSerializer,HddSerializer,CaseSerializer,PsuSerializer,QuoteSerializer

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
    if request.method == 'GET':
        queryset = MB.objects.all()
        serializer = MbSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MbSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def ram_list(request):
    if request.method == 'GET':
        queryset = RAM.objects.all()
        serializer = RamSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def vga_list(request):
    if request.method == 'GET':
        queryset = VGA.objects.all()
        serializer = VgaSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VgaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def ssd_list(request):
    if request.method == 'GET':
        queryset = SSD.objects.all()
        serializer = SsdSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SsdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def hdd_list(request):
    if request.method == 'GET':
        queryset = HDD.objects.all()
        serializer = HddSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HddSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def case_list(request):
    if request.method == 'GET':
        queryset = CASE.objects.all()
        serializer = CaseSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def psu_list(request):
    if request.method == 'GET':
        queryset = PSU.objects.all()
        serializer = PsuSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PsuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def quote_list(request):
    if request.method == 'GET':
        queryset = QUOTE.objects.all()
        serializer = QuoteSerializer(queryset, many=True)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def quote_detail(request,pk):
    try:
        quote = QUOTE.objects.get(pk=pk)
    except QUOTE.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuoteSerializer(quote)
        return Response(serializer)

    elif request.method == 'PUT':
        serializer = QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

def quote_request(request):
    data = JSONParser().parse(request)
    quote_maker = QuoteMaker()
    quote_maker.get_request(data)
    quote = quote_maker.make_quote()
    return Response(quote)
    
