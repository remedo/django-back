from django.db import models
from patient.models import Patient
from doctor.models import Doctor

# Create your models here.
class Prescription(models.Model):
    prescription_id= models.CharField(max_length=20,unique=True)
    patient_id=  models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id=  models.ForeignKey(Doctor, on_delete=models.CASCADE)
    timestamp= models.DateTimeField()
    medicines= models.BinaryField()
    reports= models.BinaryField()
    diagnosis= models.BinaryField()
    other= models.BinaryField()
    
