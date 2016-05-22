export PYTHONPATH:=.:$(PYTHONPATH)
export DJANGO_SETTINGS_MODULE:=contact.test_settings

test:
	django-admin test contact

coverage:
	coverage erase
	coverage run --branch --source=contact `which django-admin` test contact
	coverage html

clean:
	find contact -name '*.pyc' -delete
	find contact -name __pycache__ -delete
	rm -rf .coverage *.egg-info build dist htmlcov MANIFEST
