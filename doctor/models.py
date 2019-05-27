from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_id= models.CharField(max_length=20,unique=True)
    name= models.CharField(max_length=20)
    reg_no= models.CharField(max_length=20)
    spl= models.CharField(max_length=20)
    work_add= models.CharField(max_length=100)

    #last_three=models.BinaryField()
