from django import forms


class AdicionaMaterial(forms.Form):

    cafe = forms.IntegerField(label='Cafe', required=False, widget=forms.NumberInput())
    acucar = forms.IntegerField(label='Acucar', required=False, widget=forms.NumberInput())
