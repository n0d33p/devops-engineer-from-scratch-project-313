PORT ?= 8080

run: 
	uv run flask --app main run --port $(PORT) --host 0.0.0.0