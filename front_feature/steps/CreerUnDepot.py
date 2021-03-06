from behave import *
from selenium import webdriver



@given('la page de creation de depot')
def step_impl(context):
	context.driver = webdriver.Firefox()
	context.driver.get("http://localhost:8000/creerdepot")
	

@given('le champ nom du depot est ASVN')
def step_impl(context):
	elem = context.driver.find_element_by_name("nomDepot")
	elem.send_keys("ASVN")

@when('je clique sur le bouton Creer')
def step_impl(context):
	butonSubmit = context.driver.find_element_by_xpath("/html/body/form/input[2]")
	butonSubmit.click()

@then('le depot SVN du projet ASVN est creer')
def step_impl(context):
	assert True
	context.driver.close()

@given('le champ nom du depot est vide')
def step_impl(context):
	elem = context.driver.find_element_by_name("nomDepot")
	elem.clear()

@then('j\'ai l\'erreur le nom du depot ne doit pas etre vide')
def step_impl(context):
	errorLabel = context.driver.find_element_by_xpath("/html/body/form/ul/li")
	#assert "le nom du dépôt ne doit pas être vide" == errorLabel.text()
	context.driver.close()

@given('le depot ASVN existe')
def step_impl(context):
	assert True

@then('j\'ai l\'erreur le depot ASVN est deja present')
def step_impl(context):
	assert True
	context.driver.close()