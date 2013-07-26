export PYTHONPATH:=.:$(PYTHONPATH)
export DJANGO_SETTINGS_MODULE:=contact.tests.settings

test:
	django-admin.py test contact

coverage:
	coverage erase
	coverage run --branch --source=contact `which django-admin.py` test contact
	coverage html

clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage dist htmlcov MANIFEST
