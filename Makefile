PORT ?= 8080
FRAMEWORK := npx start-hexlet-devops-deploy-crud-frontend

.PHONY: test lint up down run

run:
	npx concurrently "uv run uvicorn app.main:app --host 0.0.0.0 --port $(PORT)" "$(FRAMEWORK)"

test:
	uv run pytest

lint:
	uv run ruff check .

db-up:
	docker compose up -d db

up:
	docker compose up -d
	
down:
	docker-compose down

setup: build
	uv sync
	docker-compose up -d db