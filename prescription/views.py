from django.shortcuts import render
from django.http import HttpResponse

from .models import Prescription
from django.shortcuts import render
#There's a high positive chance of this not working.
# Create your views here.
def index(request):
    return HttpResponse("Prescription")
#method to get a particular prescription
def pres_view(request,prescription_id):
    curr_pres=Prescription.objects.filter(prescription_id=prescription_id)
    context= {'pres':curr_pres}
    return render(request, 'prescription/view.html', context)
