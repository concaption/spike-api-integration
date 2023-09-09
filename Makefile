install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	python -m pytest -vv --cov=main test_*.py &&\
	python -m pytest --nbval notebook.ipynb
format:
	find src -type f -name "*.py" -print0 | xargs -0 black
lint:
	find src -type f -name "*.py" -print0 | xargs -0 pylint
refactor: format lint
run:
	uvicorn src.main:app --reload
run-docker:
	docker-compose up --build
deploy:
	# deploy goes here
all: install lint test format deploy
