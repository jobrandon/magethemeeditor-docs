PYTHON ?= python3
VENV := .venv

.PHONY: setup build verify serve

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --require-hashes -r requirements.txt
	$(VENV)/bin/python -m pip check

build:
	$(VENV)/bin/python -m mkdocs build --strict

verify: build
	$(VENV)/bin/python scripts/check_site.py

serve:
	$(VENV)/bin/python -m mkdocs serve --strict
