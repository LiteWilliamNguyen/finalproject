from django import forms
from .models import Medication, Pharmacist,Technician, Shift

class MedicationForm(forms.ModelForm):
    class Meta:
        model=Medication
        fields='__all__'

class PharmacistForm(forms.ModelForm):
    class Meta:
        model=Pharmacist
        fields='__all__'

class TechnicianForm(forms.ModelForm):
    class Meta:
        model=Technician
        fields='__all__'

class ShiftForm(forms.ModelForm):
    class Meta:
        model=Shift
        fields='__all__'