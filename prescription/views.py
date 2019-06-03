from django.http import HttpResponse
import time
from .models import Prescription
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PresForm

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
    form = PresForm()

    return render(request, 'pres.html', {'form': form})