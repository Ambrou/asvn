#-*- coding: utf-8 -*-
from django import forms

class CreerDepotForm(forms.Form):
    nomDepot = forms.CharField()

	
    def clean_nomDepot(self):
        nomDepot = self.cleaned_data['nomDepot']
        if len(nomDepot) > 100:
            raise forms.ValidationError("Trop long !")
        elif len(nomDepot) <= 0:
            raise forms.ValidationError("Trop court !")

        return nomDepot