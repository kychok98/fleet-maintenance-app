PYTHON=python3

.PHONY: run-server migration-generate migration-apply migration-apply-fake migration-apply-single

run-server:
	PYTHON manage.py runserver

migration-generate:
	PYTHON manage.py makemigrations

migration-apply:
	PYTHON manage.py migrate

migration-apply-fake:
	PYTHON manage.py migrate --fake $(APP) $(NAME)

migration-apply-single:
	PYTHON manage.py migrate $(APP) $(NAME)

default: run-server