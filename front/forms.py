#-*- coding: utf-8 -*-
from django import forms

class CreerDepotForm(forms.Form):
    nomDepot = forms.CharField(required=False, label='Nom du dépôt')

	
    def clean_nomDepot(self):
        nomDepot = self.cleaned_data['nomDepot']
        if len(nomDepot) <= 0:
            raise forms.ValidationError("le nom du dépôt ne doit pas être vide")

        return nomDepot