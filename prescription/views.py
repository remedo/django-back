from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Prescription
from django.shortcuts import render
#There's a high positive chance of this not working.
# Create your views here.
def index(request):
    return HttpResponse("Prescription")
#method to get a particular prescription
def pres_view(request,prescription_id):
    curr_pres=Prescription.objects.filter(prescription_id=prescription_id)[0]
    context= {'pres':curr_pres}
    return render(request, 'prescription/view.html', context)

def new(request):
    new_pres=Prescription()
    new_pres.prescription_id=.order_by('prescription_id')[-1]+1
    new_pres.patient_id= request.POST['patient_id']
    new_pres.doctor_id= request.POST['doctor_id']
    new_pres.medicines= request.POST['medicines']
    new_pres.diagnosis = request.POST['diagnosis']
    new_pres.timestamp = time.time()
    new_pres.others= request.POST['others']
