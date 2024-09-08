.PHONY: run-server migration-generate migration-apply migration-apply-fake migration-apply-single

run-server:
	python3 manage.py runserver

migration-generate:
	python3 manage.py makemigrations

migration-apply:
	python3 manage.py migrate

migration-apply-fake:
	python3 manage.py migrate --fake $(APP) $(NAME)

migration-apply-single:
	python3 manage.py migrate $(APP) $(NAME)

default: run-server