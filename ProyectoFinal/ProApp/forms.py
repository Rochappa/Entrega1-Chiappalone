from django import forms

class AutoFormulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()
    anio = forms.IntegerField()
    color = forms.CharField()

class MotoFormulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()
    cilindrada = forms.IntegerField()
    anio = forms.IntegerField() 

class CamionesFormulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()
    anio = forms.IntegerField()
    carga_total = forms.IntegerField()     