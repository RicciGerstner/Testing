init:
	poetry config virtualenvs.in-project true
	poetry config repositories.nexus http://lddevnexdc1:8081/repository/pypyi-internal/
	poetry install --extras all
	poetry run pre-commit install --hook-type pre-commit --install-hooks

test:
	poetry run pytest tests -v --cov

lint:
	poetry run flake8 src tests
	poetry run black src tests --check

format:
	poetry run black src tests
	poetry run isort src tests

app:
	poetry run python scripts/main.py

publish:
	poetry publish --build --repository nexus
