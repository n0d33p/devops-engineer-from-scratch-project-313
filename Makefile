# Переменные
PORT ?= 8080
DC = docker-compose
APP_CONTAINER = link_shortener_app

.PHONY: up down restart logs test lint shell

# --- Docker команды (для работы всего стека) ---

up:
	$(DC) up --build -d

down:
	$(DC) down -v

restart: down up

logs:
	$(DC) logs -f $(APP_CONTAINER)

# --- Команды разработки (внутри контейнера) ---

test:
	$(DC) exec $(APP_CONTAINER) uv run pytest

# Линтер тоже лучше гонять внутри, чтобы версии библиотек совпадали
lint:
	$(DC) exec $(APP_CONTAINER) uv run ruff check .

# Быстрый доступ к терминалу контейнера
shell:
	$(DC) exec $(APP_CONTAINER) /bin/sh