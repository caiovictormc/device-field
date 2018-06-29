env-dev:
	pip istall -r requirements/development.txt


start-dev:
	python manage.py runserver --settings=device_field.settings.development
