#-*- coding: utf-8 -*-

# Create your views here.
class ControlleurSVN():
	
	def creerRepertoire(self,nomDepot):
		print('creerRepertoire ' + nomDepot)
	
	def creerDepot(self,nomDepot):
		print('creerDepot ' + nomDepot)
	
	def modifierDroit(self,nomDepot):
		print('modifierDroit ' + nomDepot)
	
	def creer(self,nomDepot):
		self.creerRepertoire(nomDepot)
		self.creerDepot(nomDepot)
		self.modifierDroit(nomDepot)
		
	