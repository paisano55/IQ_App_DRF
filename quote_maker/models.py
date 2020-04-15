from django.db import models

class CPU(models.Model):
    maker = models.CharField(max_length=10)
    gen = models.CharField(max_length=20) #세대
    socket = models.CharField(max_length=20) #소켓
    core = models.IntegerField(max_length=3)
    thread = models.IntegerField(max_length=3)