from django.db import models

class CPU(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=10)
    gen = models.CharField(max_length=20) #세대
    socket = models.CharField(max_length=20) #소켓
    core = models.IntegerField(max_length=3)
    thread = models.IntegerField(max_length=3)
    clock = models.IntegerField(max_length=4) #MHz 단위로
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class MB(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=10)
    chipset = models.CharField(max_length=20) #칩셋
    socket = models.CharField(max_length=20) #소켓
    form = models.CharField(max_length=10) #ATX 규격
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class RAM(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    gen = models.CharField(max_length=10) #DDR
    capacity = models.IntegerField(max_length=3) #GB 단위
    clock = models.IntegerField(max_length=5) #MHz 단위
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class VGA(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    chipmaker = models.CharField(max_length=10) #엔비디아/라데온
    chipset = models.CharField(max_length=20) #1660,5700XT 등
    memcap = models.IntegerField(max_length=3) #GB 단위
    length = models.IntegerField(max_length=3) #mm 단위
    price = models.IntegerField(max_length=10) 

    def __str__(self):
        return self.name

class SSD(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    nvme = models.BooleanField()
    capacity = models.IntegerField(max_length=4) #GB 단위
    memtype = models.CharField(max_length=10) #3D TLC 등
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class HDD(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    capacity = models.IntegerField(max_length=2) #TB 단위
    rotspeed = models.IntegerField(max_length=5) #rpm 단위
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class CASE(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    size = models.CharField(max_length=10) #빅, 미들 등
    board = models.CharField(max_length=10) #최대 보드 규격
    price = models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.name

class PSU(models.Model):
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=20)
    capacity = models.IntegerField(max_length=4) # W 단위
    cert = models.CharField(max_length=10) #80+ 인증
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class Quote(models.Model):
    name = models.CharField(max_length=100)
    tot_price = models.IntegerField(default=0)
    date = models.DateTimeField()
    
    cpu = models.ForeignKey(CPU,on_delete=models.PROTECT)
    mb = models.ForeignKey(MB,on_delete=models.PROTECT)
    ram = models.ForeignKey(RAM,on_delete=models.PROTECT)
    vga = models.ForeignKey(VGA,on_delete=models.PROTECT)
    ssd = models.ForeignKey(SSD,on_delete=models.PROTECT)
    hdd = models.ForeignKey(HDD,on_delete=models.PROTECT)
    case = models.ForeignKey(CASE,on_delete=models.PROTECT)
    psu = models.ForeignKey(PSU,on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    