from django import forms
class PatientForm(forms.Form):
    patient_id= forms.CharField(label='patient_id',max_length)
    name=forms.CharField(label='Name')
    dob= forms.DateField()
    height= forms.DecimalField()
    weight= forms.DecimalField()
    add = forms.CharField(max_length=100)
    email=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=10)                
