from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Medication(models.Model):
    medname=models.CharField(max_length= 255)
    meddescription=models.TextField(null=True, blank=True)
    medusage=models.TextField(null=True, blank=True)
    medwarning=models.TextField(max_length= 255)
    medquantity=models.IntegerField()
    user=models.ForeignKey(User, on_delete = models.DO_NOTHING)
    medcost=models.IntegerField()

    def __str__(self):
        return self.medname
    
    class Meta:
        db_table = 'Medication'

class Pharmacist(models.Model):
    pharmname=models.CharField(max_length= 255)
    pharmage=models.IntegerField()
    pharmwage=models.IntegerField()
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.pharmname
    
    class Meta:
        db_table = 'Pharmacist'
    
class Technician(models.Model):
    techname=models.CharField(max_length= 255)
    techage=models.IntegerField()
    techwage=models.IntegerField()
    user=models.ManyToManyField(User)

    def __str__(self):
        return self. techname
    
    class Meta:
        db_table = 'Technician'

class Shift(models.Model):
    shiftname=models.CharField(max_length= 255)
    pharmname=models.ForeignKey(Pharmacist, on_delete=models.DO_NOTHING)
    techname=models.ForeignKey(Technician, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
