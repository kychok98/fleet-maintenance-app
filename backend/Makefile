PYTHON=python3

.PHONY: run-server make-migration apply-migration

run-server:
	PYTHON manage.py runserver

migration-generate:
	PYTHON manage.py makemigrations

migration-apply:
	PYTHON manage.py migrate
