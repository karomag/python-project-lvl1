install:
	poetry install

lint:
	poetry run flake8 brain_games

build: lint
	poetry build