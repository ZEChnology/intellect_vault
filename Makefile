ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip
PIP_INSTALL := $(PIP) install -r

$(ENV) $(PIP) env:
	python -m venv $(ENV)

deps: $(PIP)
	$(PIP_INSTALL) requirements/base.txt


.PHONY: env deps


migrations:
	env/bin/python manage.py makemigrations

migrate:
	env/bin/python manage.py migrate
