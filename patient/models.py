from django.db import models
import hashlib

# Create your models here.
class Patient(models.Model):
    patient_id= models.AutoField(primary_key=True,unique=True)
    name= models.CharField(max_length=20)
    dob= models.DateField()
    password=models.CharField(max_length=100,default=hashlib.sha256(str(0).encode()).hexdigest())
    height= models.DecimalField(decimal_places=1,max_digits=4)
    weight= models.DecimalField(decimal_places=1,max_digits=4)
    add = models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    appointments=models.BinaryField(null=True)
