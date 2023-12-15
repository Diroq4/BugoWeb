from django import forms

class DistribuidorForm(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()