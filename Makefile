install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_main.py

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb
	
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

generate_and_push:
	# Create the markdown file
	python main.md

	# Add, commit, and push the generated files to GitHub
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add .; \
	git commit -m "Add generated plots and markdown"; \
	git push; \

all: install format lint test
