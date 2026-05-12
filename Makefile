PORT ?= 8080
FRAMEWORK := npx start-hexlet-devops-deploy-crud-frontend

.PHONY: test lint up down run db-up setup

run:
	npx concurrently "uv run uvicorn app.main:app --host 0.0.0.0 --port $(PORT)" "$(FRAMEWORK)"

test:
	PYTHONPATH=. uv run pytest

lint:
	uv run ruff check .

db-up:
	docker compose up -d db

up:
	docker compose up -d
	
down:
	docker compose down

setup:
	uv sync