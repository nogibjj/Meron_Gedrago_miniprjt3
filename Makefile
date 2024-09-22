install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb
	
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint


all: install format lint test
