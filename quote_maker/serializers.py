from rest_framework import serializers
from .models import CPU,MB,RAM,VGA,SSD,HDD,CASE,PSU,Quote

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ('')