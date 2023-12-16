from django import forms

class DistribuidorForm(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()

class BusquedaDistribuidorForm(forms.Form):
    nombre = forms.CharField()

class ContactanosForm(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()