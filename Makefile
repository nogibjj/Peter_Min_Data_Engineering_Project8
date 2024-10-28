format:
	cargo fmt

check:
	cargo check

lint:
	cargo clippy

py_format:
	black *.py

py_lint:
	ruff check *.py mylib/*.py

py_refactor:
	py_format py_lint

py_test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py