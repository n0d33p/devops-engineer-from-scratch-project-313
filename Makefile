PORT ?= 8080
FRAMEWORK := npx start-hexlet-devops-deploy-crud-frontend

.PHONY: test lint up down run

run:
	npx concurrently "uv run uvicorn main:app --host 0.0.0.0 --port $(PORT)" "$(FRAMEWORK)"

test:
	uv run pytest

lint:
	uv run ruff check .

up:
	docker compose up -d db

down:
	docker-compose down