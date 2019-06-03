from django import forms

class PresForm(forms.Form):
    prescription_id = forms.CharField(label='ID', max_length=100)

