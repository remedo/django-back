from django.db import models
from patient.models import Patient
from doctor.models import Doctor
from django.utils import timezone
# Create your models here.
class Prescription(models.Model):
    prescription_id= models.CharField(max_length=50,unique=True)
    patient_id=  models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id=  models.ForeignKey(Doctor, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(timezone.now())
    medicines= models.BinaryField()
    reports= models.BinaryField()
    diagnosis= models.BinaryField()
    other= models.BinaryField()
