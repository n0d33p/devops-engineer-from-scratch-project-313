PORT ?= 8080
# В Alpine убедись, что npx доступен (ты добавил nodejs/npm в apk add, это верно)
FRAMEWORK := npx start-hexlet-devops-deploy-crud-frontend

.PHONY: test lint up down run db-up setup

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
	# Убираем дефис и флаг -v для стабильности в CI
	docker compose down

setup:
	uv sync