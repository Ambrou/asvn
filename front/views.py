#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from front.forms import CreerDepotForm

# def creerDepot(request):
	# if request.method == 'POST':  # S'il s'agit d'une requête POST
		# form = CreerDepotForm(request.POST)  # Nous reprenons les données

		# if form.is_valid(): # Nous vérifions que les données envoyées sont valides

			# # Ici nous pouvons traiter les données du formulaire
			# nomDepot = form.cleaned_data['nomDepot']
		

	# else: # Si ce n'est pas du POST, c'est probablement une requête GET
		# form = CreerDepotForm()  # Nous créons un formulaire vide

	# return render(request, 'creerDepot.html', locals())


# Create your views here.
class AboutView(View):
	form_class = CreerDepotForm
	initial = {'key': 'value'}
	template_name = 'creerDepot.html'

	def get(self, request, *args, **kwargs):
		# return HttpResponse('Hello, World!')
		form = self.form_class()
		# return render(request, self.template_name, {'form': form})
		return render(request, 'creerDepot.html', locals())
		
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# <process form cleaned data>
			nomDepot = form.cleaned_data['nomDepot']

		return render(request, self.template_name, {'form': form})