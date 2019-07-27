from django.shortcuts import render
from .models import Doctor,appointment,slot
from patient.models import Patient
from prescription.models import Prescription
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import hashlib
from django.core.paginator import Paginator
from pickle import loads,dumps
from datetime import datetime,timedelta


# methods being used
def verify(request):
    if ("user" in request.session) and (request.session.get("user_type")=="doctor"):
        return True
# Create your views here.
def login(request):
    if (request.method=="POST"):
        if "doctor_id" in request.POST:
            d=Doctor.objects.get(doctor_id=request.POST.get("doctor_id"))
            if d.password==hashlib.sha256(str(request.POST.get("password")).encode()).hexdigest():
                print(d.password,hashlib.sha256(str(request.POST.get("password")).encode()).hexdigest())
                request.session["user_type"]="doctor"
                request.session["user"]=d.doctor_id
                return HttpResponseRedirect('dash')
    return render(request,'doctor/login.html',{ "message":"Login"})
def change_pass(request):
    if request.method == "POST":
        if verify(request):
            d=Doctor.objects.get(doctor_id=request.session.get("user"))
            if d.password==hashlib.sha256(str(request.POST.get("old_password")).encode()).hexdigest():
                d.password=hashlib.sha256(str(request.POST.get("new_password")).encode()).hexdigest()
                d.save()
                del request.session["user"]
                del request.session["user_type"]
                request.session.modified = True
                return render(request,'doctor/login.html',{'message':"Password Change Succesful . Login"})
        else:
            return render(request,'doctor/change_pass.html',{'message':"Password change unsuccesful . Try Again"})
    return render(request,'doctor/change_pass.html')
def logout(request):
        del request.session["user"]
        del request.session["user_type"]
        request.session.modified = True
        return render(request,'doctor/login.html',{'message':"Log Out Successful"})
def dashboard(request):
    if verify(request):
            return HttpResponseRedirect('prescriptions')
    else:
            return render(request,'doctor/login.html',{'message':"Login Failed. Try Again."})

def prescriptions(request):
    if verify(request):
        d=Doctor.objects.get(doctor_id=request.session.get("user"))
        prescription_list=Prescription.objects.filter(doctor_id=d) #requesting prescription for current user.
        paginator=Paginator(prescription_list,5) # number of prescription at a time is choosen to be 15
        page= request.GET.get('page') # getting the current page
        prescriptions=paginator.get_page(page) #list of prescriptions to be taken at a time
        context={'doctor':d,'prescriptions':prescriptions}
        return render(request,'doctor/prescriptions.html',context)
    else:
        return render(request,'doctor/login.html',{'message':"Please Login First."})
def search(request):
    if verify(request):
        d=Doctor.objects.get(doctor_id=request.session.get("user"))
        prescription_list= Prescription.objects.filter(patient_id=Patient.objects.get(patient_id=request.POST.get("search_text")))
        paginator=Paginator(prescription_list,5) # number of prescription at a time is choosen to be 15
        page= request.GET.get('page') # getting the current page
        prescriptions=paginator.get_page(page) #list of prescriptions to be taken at a time
        context={'doctor':d,'prescriptions':prescriptions}
        return render(request,'doctor/prescriptions.html',context)

def slots_setter(request):
    print(request.method)
    d=Doctor.objects.get(doctor_id=request.session.get("user"))
    if verify(request) and request.method=="POST":
        i="1"
        breaks=[]
        while(("break_start_time"+i) in request.POST ):
            breaks.append([datetime.strptime(request.POST.get("break_start_time"+i),"%H:%M"),datetime.strptime(request.POST.get("break_end_time"+i),"%H:%M")])
            i=str(int(i)+1)

        i="1"

        days_off=[]
        while(("day"+i) in request.POST ):
            days_off.append([request.POST.get("day"+i)])
            i=str(int(i)+1)

        slots=slot(request.POST.get("start_time"),request.POST.get("end_time"),request.POST.get("slot_interval"),breaks,days_off)
        print(type(slots.start_time))
        slot_db=dumps(slots)
        d.slots=slot_db
        d.save()
        return HttpResponseRedirect('prescriptions')
    return render(request,'doctor/slots_setter.html',{'doctor':d})

def get_slots(request):
    if request.method=="POST":
        if verify(request):
            date = request.POST.get("date")
            request.session["date"]=date
            d= Doctor.objects.get(doctor_id=request.session.get("user"))
            slots=loads(d.slots)
            print(datetime.strptime(slots.start_time,"%H:%M"))
            total_slots=set([str((datetime.strptime(slots.start_time,"%H:%M")+ timedelta(minutes=x)).hour)+":" +str((datetime.strptime(slots.start_time,"%H:%M")+ timedelta(minutes=x)).minute)  for x in range(0,int(((datetime.strptime(slots.end_time,"%H:%M"))-(datetime.strptime(slots.start_time,"%H:%M"))).total_seconds()/60),int(slots.slot_interval))])
            print(total_slots)
            if loads(d.appointments) is not None:
                appointments=loads(d.appointments)
                for appointment in appointments:

                    if appointment.date==date:
                        print(total_slots,set(appointment.slot))

                        total_slots -= set([appointment.slot])
            message="Select slots"
            return render(request,'doctor/appointments.html',{'doctor':d,'message':message,'total_slots':total_slots})


def add_appointment(request):
    if verify(request):
        d= Doctor.objects.get(doctor_id=request.session.get("user"))
        message="Choose a Date"


        if request.method=='POST':
            date=request.session.get("date")
            slots=request.POST.getlist("slots")
            patient_id=request.POST.get("patient_id")

            if loads(d.appointments) is not None:
                appointments=loads(d.appointments)
            else:
                appointments=[]

            for slot in slots:
                appointments.append(appointment(patient_id,date, slot))
            message="Successfuly Added Appointment"
            d.appointments = dumps(appointments)
            d.save()
            return render(request,'doctor/appointments.html',{'doctor':d,'message':message})
        return render(request,'doctor/appointments.html',{'doctor':d,'message':message})
