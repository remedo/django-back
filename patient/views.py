from django.shortcuts import render
from .models import Patient
from prescription.models import Prescription
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import hashlib
from django.core.paginator import Paginator


# Login View for user type patient
def login(request):
    if (request.method=="POST"):
        if "email" in request.POST:
            p=Patient.objects.filter(email=request.POST.get("email"))[0]
            print(p.patient_id,hashlib.sha256(str(request.POST.get("password")).encode()).hexdigest(),p.password)
            if p.password==hashlib.sha256(str(request.POST.get("password")).encode()).hexdigest():
                request.session["user_type"]="patient"
                request.session["user"]=p.patient_id
                return HttpResponseRedirect('dash')
    return render(request,'patient/login.html',{ "message":"Login"})
def change_pass(request):
    if request.method == "POST":
        if "user" in request.session and request.session.get("user_type")=="patient":
            p=Patient.objects.get(patient_id=request.POST.get("patient_id"))
            if p.password==hashlib.sha256(str(request.POST.get("old_password")).encode()).hexdigest():
                p.password=hashlib.sha256(str(request.POST.get("new_password")).encode()).hexdigest()
                p.save()
                del request.session["user"]
                del request.session["user_type"]
                request.session.modified = True
                return render(request,'patient/login.html',{'message':"Password Change Succesful . Login"})
        else:
            return render(request,'patient/change_pass.html',{'message':"Password change unsuccesful . Try Again"})
    return render(request,'patient/change_pass.html')
def logout(request):
        del request.session["user"]
        del request.session["user_type"]
        request.session.modified = True
        return render(request,'patient/login.html',{'message':"Log Out Successful"})
def dashboard(request):
    if ("user" in request.session) and (request.session.get("user_type")=="patient"):
            return HttpResponseRedirect('prescriptions')
    else:
            return render(request,'patient/login.html',{'message':"Login Failed. Try Again."})

def prescriptions(request):
    p=Patient.objects.get(patient_id=request.session.get("user"))

    prescription_list=Prescription.objects.filter(patient_id=p) #requesting prescription for current user.
    print(prescription_list)
    paginator=Paginator(prescription_list,15) # number of prescription at a time is choosen to be 15
    page= request.GET.get('page') # getting the current page
    prescriptions=paginator.get_page(page) #list of prescriptions to be taken at a time
    context={'patient':p,'prescriptions':prescriptions}
    return render(request,'patient/prescriptions.html',context)
