FROM node:20 AS frontend-builder
WORKDIR /build
COPY package.json package-lock.json* ./
RUN npm install

FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


RUN apk add --no-cache \
    build-base \
    curl \
    git \
    bash \
    make \
    nodejs \
    npm \
    nginx

WORKDIR /app


COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

COPY app/ ./app/
COPY nginx.conf /etc/nginx/http.d/default.conf

COPY --from=frontend-builder /build/node_modules/@hexlet/project-devops-deploy-crud-frontend/dist /app/public

RUN echo -e "#!/bin/sh\nnginx & uv run gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 app.main:app" > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]