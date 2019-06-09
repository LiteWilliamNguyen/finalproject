from django.contrib import admin
from .models import Medication,Pharmacist,Technician,Shift

# Register your models here.
admin.site.register(Medication)
admin.site.register(Pharmacist)
admin.site.register(Technician)
admin.site.register(Shift)
