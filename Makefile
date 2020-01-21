NAME=ngs360-flask
.PHONY: clean install build test lint test-frontend run shell

all: clean install test lint build

clean:
	find . -name __pycache__ -exec rm -rf {} +
	rm -rf *.pyc .coverage .pytest_cache/ htmlcov/ .venv/ .env test.db

install: requirements.txt requirements-dev.txt
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt && pip install -r requirements-dev.txt

build:
	docker build -t $(NAME) .

test:
	rm -rf .env test.db .coverage htmlcov/
	source .venv/bin/activate && python -m pytest -vv --cov app/ --ignore=tests/FrontEnd && coverage html

lint:
	source .venv/bin/activate && PYTHONPATH="." pylint app tests --load-plugins pylintplugins,pylint_flask_sqlalchemy --exit-zero

test-frontend:
	rm -rf .env test.db
	source .venv/bin/activate && python3 -m pytest -v tests/FrontEnd

docker-run:
	docker run --rm -ti -v app.db:/app/app.db -p 5000:5000 $(NAME)

run:
	source .venv/bin/activate && flask db upgrade && python application.py

shell:
	source .venv/bin/activate && flask shell
