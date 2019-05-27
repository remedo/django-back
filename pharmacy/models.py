from django.db import models

# Create your models here.
class pharmacy(models.Model):
    pharm_id= models.CharField(max_length=20,unique=True)
    name= models.CharField(max_length=30)
    medicines= models.BinaryField()
