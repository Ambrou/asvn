#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from front.forms import CreerDepotForm

# Create your views here.
class CreerDepotView(FormView):
	template_name = 'creerDepot.html'
	form_class = CreerDepotForm

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, locals())
		
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# <process form cleaned data>
			nomDepot = form.cleaned_data['nomDepot']

		return render(request, self.template_name, {'form': form})