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

generate_and_push:
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add main.py summary_report.md; \
	git commit -m "Add generated plot and report"; \
	git push; \


all: install format lint test
