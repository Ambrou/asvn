#-*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

#-*- coding: utf-8 -*-
# from django.http import HttpResponse

# def creerDepot(request):
  # text = """<h1>Bienvenue sur mon blog !</h1>
            # <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
  # return HttpResponse(text)
#
#-*- coding: utf-8 -*-
from django.http import HttpResponse
from front.forms import CreerDepotForm

def creerDepot(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CreerDepotForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            message = form.cleaned_data['message']
            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = CreerDepotForm()  # Nous créons un formulaire vide

    return render(request, 'creerDepot.html', locals())