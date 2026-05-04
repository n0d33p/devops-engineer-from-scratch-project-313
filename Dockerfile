FROM node:20 AS frontend-builder

WORKDIR /build

COPY package.json package-lock.json* ./
RUN npm install

FROM python:3.12-slim

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

COPY app/ ./app/
COPY nginx.conf /etc/nginx/sites-available/default

COPY --from=frontend-builder /build/node_modules/@hexlet/project-devops-deploy-crud-frontend/dist /app/public

RUN echo "#!/bin/bash\nnginx -g 'daemon off;' & uv run gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 app.main:app" > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]