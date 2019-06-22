from django.shortcuts import render
from .models import Patient
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import hashlib

# Create your views here.
def login(request,message):
    if (request.method=="POST"):
        if "email" in request.POST:
            p=Patient.objects.filter(email=request.POST.get("email"))[0]
            if p.password==hashlib.sha256(str(request.POST.get("password")).encode()).hexdigest():
                request.session["user_type"]="patient"
                request.session["user"]=p.patient_id
                return HttpResponseRedirect('/dash/')
    return render(request,'patient/login.html')
def change_pass(request):
    if request.method == "POST":
        if "user" in request.session and request.session.get("user_type")=="patient":
            p=Patient.objects.get(patient_id=request.POST.get("patient_id"))
            if p.password==hashlib.sha256(str(request.POST.get("old_password")).encode()).hexdigest():
                p.password=request.POST.get("new_password")
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
    if (request.method=="POST"):
        if ("user" in request.session) and (request.session.get("user_type")=="patient"):
            p=Patient.objects.get(patient_id=request.session.get("user"))
            context={'patient':p}
            return render(request,'patient/dash.html',context)
        else:
            return render(request,'patient/login.html',{'message':"Login Failed. Try Again."})
