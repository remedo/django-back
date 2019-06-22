from django.http import HttpResponse,HttpResponseRedirect
import datetime
from .models import Prescription
from patient.models import Patient
from doctor.models import Doctor
from django.shortcuts import render
from pickle import dumps,loads
#There's a high positive chance of this not working.
# Create your views here.
def index(request):
    return HttpResponse("Prescription")
# method to get a particular prescription
def display(request,prescription_id):
    curr_pres=Prescription.objects.filter(prescription_id=id)[0]
    context= {'pres':curr_pres,'medicines':loads(curr_pres.medicines),'diagnosis':loads(curr_pres.diagnosis)}
    return render(request, 'prescription/view.html', context)
def pres_view(request):
    if request.method=="POST":
        if request.POST.get("patient_id"):
            pres=Prescription()
            timestamp=datetime.datetime.now()
            id=str(request.POST.get("patient_id"))+"."+str(request.session.get("doctor_id"))+"."+str(timestamp.year)+str(timestamp.month)+str(timestamp.day)+str(timestamp.hour)+str(timestamp.minute)
            pres.prescription_id=id
            pres.patient_id=Patient.objects.get(patient_id=request.POST.get("patient_id"))
            pres.doctor_id=Doctor.objects.get(doctor_id=request.session.get("doctor_id"))
            pres.timestamp=timestamp
            i="1"
            medicines=[]
            diagnosis=[]
            while(("medicinesName"+i) in request.POST ):
                medicines.append([request.POST.get("medicinesName"+i),request.POST.get("medicinesDPD"+i),request.POST.get("medicinesNOD"+i),request.POST.get("medicinesNotes"+i)])
                i=str(int(i)+1)
            i="1"
            while(("diagnosis"+i) in request.POST ):
                diagnosis.append(request.POST.get("diagnosis"+i))
                i=str(int(i)+1)
            pres.medicines=dumps(medicines)
            pres.diagnosis=dumps(diagnosis)
            pres.save()

    curr_pres=Prescription.objects.filter(prescription_id=id)[0]
    context= {'pres':curr_pres,'medicines':loads(curr_pres.medicines),'diagnosis':loads(curr_pres.diagnosis)}
    return render(request, 'prescription/view.html', context)


def new(request):
    request.session['doctor_id']="0"
    return render(request, 'prescription/pres.html')
