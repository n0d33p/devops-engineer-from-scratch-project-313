PORT ?= 8080
ifneq ($(GITHUB_ACTIONS),)
    RUN_APP = uv run
else
    DC = docker compose
    APP_CONTAINER = link_shortener_app
    RUN_APP = $(DC) exec $(APP_CONTAINER) uv run
endif

.PHONY: test lint up down run shell logs

run:
	uv run uvicorn main:app --host 0.0.0.0 --port $(PORT)

test:
	$(RUN_APP) pytest

lint:
	$(RUN_APP) ruff check .

up:
	$(DC) up --build -d

down:
	$(DC) down -v

logs:
	$(DC) logs -f $(APP_CONTAINER)

shell:
	$(DC) exec $(APP_CONTAINER) /bin/sh