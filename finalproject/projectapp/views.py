from django.shortcuts import render, get_object_or_404
from .models import Medication, Pharmacist, Technician, Shift
from .forms import MedicationForm, PharmacistForm, TechnicianForm, ShiftForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'projectapp/index.html')

def getMedication(request):
    med_list=Medication.objects.all()
    context={'med_list' : med_list}
    return render(request,'projectapp/med.html', context=context)

def getPharmacist(request):
    pharmacist_list=Pharmacist.objects.all()
    context={'pharmacist_list' : pharmacist_list}
    return render(request, 'projectapp/pharmacist.html', context=context)

def getTechnician(request):
    technician_list=Technician.objects.all()
    context={'technician_list' : technician_list}
    return render(request, 'projectapp/technician.html', context=context)

def getShift(request):
    shift_list=Shift.objects.all()
    context={'shift_list' : shift_list}
    return render(request, 'projectapp/shift.html', context=context)

def shiftdetail(request, id):
    shift=get_object_or_404(Shift, pk=id)
    medcount=Medication.objects.filter(user=id).count()
    medication=Medication.objects.filter(user= id)
    pharmacist=Pharmacist.object.filter(user= id)
    technician=Technician.object.filter(user= id)
    context={
        'shift' :shift,
        'medcount' : medcount,
        'medication' : medication,
        'pharmacy' : pharmacy,
        'technician' : technician

    }
    return render (request, 'finalproject/shiftdetail.html', context = context)

def newMedication(request):
    form=MedicationForm
    if request.method =='POST':
        form=MedicationForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MedicationForm()
    else:
        form=MedicationForm()
    return render(request, 'projectapp/newmedication.html', {'form': form})
@login_required
def newPharmacist(request):
    form=PharmacistForm
    if request.method =='POST':
        form=PharmacistForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=PharmacistForm()
    else:
        form=PharmacistForm()
    return render(request, 'projectapp/newpharmacist.html', {'form': form})
@login_required
def newTechnician(request):
    form=TechnicianForm
    if request.method =='POST':
        form=TechnicianForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TechnicianForm()
    else:
        form=TechnicianForm()
    return render(request, 'projectapp/newtechnician.html', {'form': form})

def newShift(request):
    form=ShiftForm
    if request.method =='POST':
        form=ShiftForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ShiftForm()
    else:
        form=TechnicianForm()
    return render(request, 'projectapp/shift.html', {'form': form})

def loginMessage(request):
    return render(request, 'projectapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'projectapp/logoutmessage.html')