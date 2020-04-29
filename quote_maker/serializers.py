from rest_framework import serializers
from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,Quote

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ('id','name','maker','gen','socket','core','thread','clock','price')

class MbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MB
        fields = ('id','name','maker','chipset','socket','form','price')

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM 
        fields = ('id','name','maker','gen','capactity','clock','price')

class VgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VGA 
        fields = ('id','name','maker','chipmaker','chipset','memcap','length','price')

class SsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD 
        fields = ('id','name','maker','nvme','capacity','memtype','price')

class HddSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD 
        fields = ('id','name','maker','capacity','rotspeed','price')

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CASE 
        fields = ('id','name','maker','size','board','price')

class PsuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSU 
        fields = ('id','name','maker','capacity','cert','price','price')
