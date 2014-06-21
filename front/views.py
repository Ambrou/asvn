#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from front.forms import CreerDepotForm

def creerDepot(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = CreerDepotForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides

			# Ici nous pouvons traiter les données du formulaire
			nomDepot = form.cleaned_data['nomDepot']
		

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = CreerDepotForm()  # Nous créons un formulaire vide

	return render(request, 'creerDepot.html', locals())