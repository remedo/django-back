from django.db import models

# Create your models here.
class medicine(models.Model):
    med_id= models.CharField(max_length=20,unique=True)
    name= models.CharField(max_length=30)
    doe=models.DateField()
    manufacturer=models.CharField(max_length=100)
