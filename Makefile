install:
	pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py

refactor: format lint

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py