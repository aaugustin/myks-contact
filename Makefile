test:
	python -m django test --settings=contact.test_settings

coverage:
	coverage erase
	coverage run -m django test --settings=contact.test_settings
	coverage html

clean:
	rm -rf .coverage dist contact.egg-info htmlcov

style:
	flake8 contact
