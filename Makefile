install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_main.py

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb

all: install format lint test
