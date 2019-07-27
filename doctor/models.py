from django.db import models
import hashlib
from pickle import loads


# Create your models here.
class Doctor(models.Model):
    doctor_id= models.AutoField(primary_key=True,unique=True)
    name= models.CharField(max_length=20)
    reg_no= models.CharField(max_length=20)
    spl= models.CharField(max_length=20)
    work_add= models.CharField(max_length=100)
    password=models.CharField(max_length=100,default=hashlib.sha256(str(doctor_id).encode()).hexdigest())
    phone=models.CharField(max_length=10,default="0")
    slots=models.BinaryField(null=True)
    appointments=models.BinaryField(null=True)
    def appointment_available(self,date,slots):
        appointments= loads(self.appointments)
        for slot in slots:
            if slot in appointment[date]:
                return str(slot)+" not available on"+ str(date)
        else:
            return "Available"
class appointment:
    def __init__(self,patient_id,date,slot):
        self.patient_id=patient_id
        self.date=date
        self.slot=slot

class slot:
    def __init__(self,start_time,end_time,slot_interval,breaks,days_off=[],dates_off=[]):
        self.start_time=str(datetime.strptime(start_time,"%H:%M").hour)+":"+str(datetime.strptime(start_time,"%H:%M").minute)
        self.end_time=str(datetime.strptime(end_time,"%H:%M").hour)+":"+str(datetime.strptime(end_time,"%H:%M").minute)
        self.slot_interval=slot_interval
        self.days_off=days_off
        self.dates_off=dates_off
        self.breaks=breaks
